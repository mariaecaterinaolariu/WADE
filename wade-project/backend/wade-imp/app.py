import time
import cv2
from SPARQLWrapper import SPARQLWrapper, GET, JSON
from flask import Flask, Response, request, send_from_directory, jsonify, send_file
import base64
from flask_cors import CORS
from deepface import DeepFace
import os
import deepfacewiki
import mongodb
import ontology_blazegraph_poc
import json
from rdflib.plugins.sparql import prepareQuery

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload-image', methods=['POST','GET'])
def upload_file():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        if os.path.isfile(os.path.join(UPLOAD_FOLDER, file.filename)):
            # Create new entity for the portrait and the painter and add to database
            filepath = UPLOAD_FOLDER + "/" + file.filename.split(" ")[0]
            portrait_entity = deepfacewiki.create_portrait_new_entity(filepath, file.filename)
            mongodb.add_entity_to_collection('portraits', portrait_entity)
            time.sleep(1)
            painter_entity = deepfacewiki.create_painter_new_entity(file.filename)
            mongodb.add_entity_to_collection('painters', painter_entity)
            time.sleep(1)
            #Add to stupid blazegraph
            ontology_blazegraph_poc.add_portrait_entity_to_graph(portrait_entity)
        return jsonify({'message': 'File uploaded successfully'}), 200

@app.route('/images')
def get_images():
    images = []
    for filename in os.listdir(UPLOAD_FOLDER):
        if filename.endswith(('.jpg', '.png', '.jpeg')):
            images.append(filename)
    return jsonify(images)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    print(filename)
    image = send_from_directory(UPLOAD_FOLDER, filename.split(" ")[0])
    return image

@app.route('/analyze/facedetect/<filename>')
def analyze_image(filename):
    image = send_from_directory(UPLOAD_FOLDER, filename)
    print(type(image))
    print(image)
    filepath = UPLOAD_FOLDER + "/" + filename.split(" ")[0]
    print(filepath)
    imageInfo = deepfacewiki.get_image_deepface_info(filepath)
    newImage = deepfacewiki.see_faces(filepath, imageInfo)
    print(type(newImage))
    print(newImage.shape)
    _, img_encoded = cv2.imencode('.jpg', newImage)
    response = Response(response=img_encoded.tobytes(), status=200, mimetype='image/jpeg')
    print(response)
    return response

@app.route('/analyze/emotions/<filename>')
def analyze_emotions(filename):
    filepath = UPLOAD_FOLDER + "/" + filename.split(" ")[0]
    imageInfo = deepfacewiki.get_image_deepface_info(filepath)
    return jsonify(imageInfo)

@app.route('/painters-name', methods=['GET'])
def get_painters_name():
    with open('painters.json', 'r') as file:
        painters_data = json.load(file)
    painter_names = [data['painter'] for data in painters_data.values()]
    return jsonify(painter_names)

@app.route('/painters')
def get_painters():
    names,pictures = deepfacewiki.get_names_from_files(UPLOAD_FOLDER)
    return {'names:': list(names), 'pictures': pictures}

@app.route('/painters/<name>')
def get_painter(name):
    summary, lifespan, originalImage = deepfacewiki.get_wikipedia_summary(name)
    return {'summary': summary, 'lifespan': lifespan, 'image': originalImage}

@app.route('/filter', methods=['GET'])
def filter_query():
    # Get query parameters
    race = request.args.get('race', default=None)
    gender = request.args.get('gender', default=None)
    emotion = request.args.get('emotion', default=None)

    sparql = SPARQLWrapper("http://localhost:9999/blazegraph/sparql")
    sparql.method = "GET"

    sparql_query = """
    PREFIX onto: <http://example.org/ontology/>
    
        SELECT DISTINCT ?portrait
        WHERE {"""

    filters = []
    if race:
        sparql_query += f"?portrait onto:hasRace ?race ."
    if gender:
        sparql_query += f"?portrait onto:hasGender ?gender .\n"
    if emotion:
        sparql_query += f"?portrait onto:hasEmotion ?emotion .\n"

    if race:
        races = [f"onto:{e.capitalize()}" for e in race.split(',')]
        races_filter = "(" + ' || '.join([f"?race = {e}" for e in races]) + ")"
        filters.append(races_filter)
    if gender:
        genders = [f"onto:{e.capitalize()}" for e in gender.split(',')]
        genders_filter = "(" + ' || '.join([f"?gender = {e}" for e in genders]) + ")"
        filters.append(genders_filter)
    if emotion:
        emotions = [f"onto:{e.capitalize()}" for e in emotion.split(',')]
        emotion_filter = "(" + ' || '.join([f"?emotion = {e}" for e in emotions]) + ")"
        filters.append(emotion_filter)

    if filters:
        sparql_query += "FILTER(" + " && ".join(filters) + ")}\n"

    sparql.setQuery(sparql_query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    image_filenames = []
    for result in results["results"]["bindings"]:
        uri = result["portrait"]["value"]
        # Extract the filename from the URI
        filename = os.path.basename(uri) + ".jpg"
        image_filenames.append(filename)

    return jsonify({'images': image_filenames})

if __name__ == '__main__':
    app.run(debug=True)

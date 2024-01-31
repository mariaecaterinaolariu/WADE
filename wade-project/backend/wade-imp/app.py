from flask import Flask, request, send_from_directory, jsonify, send_file
import base64
from flask_cors import CORS
from deepface import DeepFace
import os
import deepfacewiki

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload-image', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
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
    return send_from_directory(UPLOAD_FOLDER, filename.split(" ")[0])

@app.route('/painters')
def get_painters():
    names,pictures = deepfacewiki.get_names_from_files(UPLOAD_FOLDER)
    return {'names:': list(names), 'pictures': pictures}

@app.route('/painters/<name>')
def get_painter(name):
    summary, lifespan, originalImage = deepfacewiki.get_wikipedia_summary(name)
    return {'summary': summary, 'lifespan': lifespan, 'image': originalImage}

if __name__ == '__main__':
    app.run(debug=True)

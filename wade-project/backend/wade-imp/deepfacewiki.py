
import base64
import json
import os
import re
import time
import cv2
from deepface import DeepFace
import requests


def get_names_from_files(directory):
    # Initialize an empty set to store unique names
    names = set()
    pictures = 0
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        pictures +=1
        # If the filename matches the pattern "name_number.jpg"
        match = re.match(r'([a-z-]+)_\d+\.jpg$', filename)
        if match:
            # Extract the name, replace hyphens with underscores, and capitalize each part
            name = match.group(1).replace('-', '_').title()
            # Add the name to the set (this automatically removes duplicates)
            names.add(name)

    return (names, pictures)

def get_wikipedia_summary(title):
    # Define the endpoint
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"

    # Send a GET request to the Wikipedia API
    response = requests.get(url)

    # If the request was successful, return the summary and lifespan
    if response.status_code == 200:
        summary = response.json()["extract"]
        description = response.json()["description"]
        originalImage = response.json()["originalimage"]["source"]
        # Try to find a lifespan in the summary
        lifespan_match = re.search(r'\((\d{4})\s*–\s*(\d{4})\)', description)
        if not lifespan_match:
            lifespan_match = re.search(r'\((\d{4})\s*–\s*(\d{4})\)', summary)
        if lifespan_match:
            birth_year, death_year = lifespan_match.groups()
            lifespan = f"{birth_year} - {death_year}"
        else:
            lifespan = "Lifespan not found in summary."
        if summary == None:
            return "No summary information available.", lifespan, originalImage
        if originalImage == None:
            return summary, lifespan, "originalImage not found in summary."
        return summary, lifespan, originalImage 
    else:
        return "No summary information available.", "Lifespan not found in summary.", "originalImage not found in summary."

def get_image_deepface_info(image_path):
    try:
        print(image_path)
        # Assuming the function that might raise a ValueError is DeepFace.analyze()
        result = DeepFace.analyze(img_path = image_path, 
            actions = ['age', 'gender', 'race', 'emotion'])
        time.sleep(5)
        objs = result # or whatever key you're interested in
    except ValueError:
        # This block will run if DeepFace.analyze() raises a ValueError
        objs = None

    if objs is None or objs == 0:
        print("No face detected or an error occurred.")

    return objs

def see_faces(image_path, objs):
    image = cv2.imread(image_path)
    for prediction in objs:
        x = prediction['region']['x']
        y = prediction['region']['y']
        w = prediction['region']['w']
        h = prediction['region']['h']

        start_point = (x, y) # The start coordinate (x, y)
        end_point = (x+w, y+h) # The end coordinate (x+w, y+h)
        color = (255, 0, 0) # RGB color code for the border
        thickness = 2 # Thickness of the border

        cv2.rectangle(image, start_point, end_point, color, thickness)

    #cv2.imshow('Faces: ', image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    return image

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
        
# create json file with data from deepface for each painting in uploads folder
def create_json_portraits(directory):
    data = {}
    index = 0
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"): 
            path = os.path.join(directory, filename)
            image_info = encode_image(path)
            #wikipedia_info = get_wikipedia_summary(path)
            deepface_info = get_image_deepface_info(path)
            if deepface_info == None:
                print("No face detected or an error occurred.")
                continue
            print(filename.split('_')[0])
            data[index] = {
                'filename': filename,
                'emotion': deepface_info[0]['dominant_emotion'],
                'age': deepface_info[0]['age'],
                'race': deepface_info[0]['dominant_race'],
                'image_encoding': image_info,
                'face_positions': deepface_info[0]['region'],
                'painter': filename.split('_')[0],
                'deepface_info': deepface_info
            }
            
            index += 1
    with open('portraits.json', 'w') as outfile:
        json.dump(data, outfile)
# create a json file with data from wikipedia for each painter in uploads folder
def create_json_painters(directory):
    data = {}
    index = 0

    painters = set()
    for filename in os.listdir(directory):
        painter = filename.split('_')[0]
        painter = painter.replace('-', '_')
        painters.add(painter)
    painters = list(painters)
    for painter in painters:
        summary, lifespan, originalImage = get_wikipedia_summary(painter)
        data[index] = {
            'painter': painter,
            'summary': summary,
            'lifespan': lifespan,
            'originalImage': originalImage
        }
        index += 1
    
    with open('painters.json', 'w') as outfile:
        json.dump(data, outfile)

#create_json_painters('uploads')
#create_json_portraits('uploads')
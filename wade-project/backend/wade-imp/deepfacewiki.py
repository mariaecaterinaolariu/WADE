
import os
import re
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
        return summary, lifespan, originalImage 
    else:
        return "No summary information available.", "Lifespan not found in summary.", originalImage

def get_image_deepface_info(image_path):
    try:
        print(image_path)
        # Assuming the function that might raise a ValueError is DeepFace.analyze()
        result = DeepFace.analyze(img_path = image_path, 
            actions = ['age', 'gender', 'race', 'emotion'])
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
    
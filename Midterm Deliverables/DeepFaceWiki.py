import re
import os
from deepface import DeepFace
from PIL import Image
import requests
import cv2 

def get_names_from_files(directory):
    names = set()
    pictures = 0

    for filename in os.listdir(directory):
        pictures +=1
        # If the filename matches the pattern "name_number.jpg"
        match = re.match(r'([a-z-]+)_\d+\.jpg$', filename)
        if match:
            name = match.group(1).replace('-', '_').title()
            # Add the name to the set - automatically removes duplicates
            names.add(name)

    return names, pictures


def get_image_metadata(image_path):
    with Image.open(image_path) as img:
        metadata = img.info
    return metadata


def get_image_deepface_info(image_path):
    objs = DeepFace.analyze(img_path = image_path, 
            actions = ['age', 'gender', 'race', 'emotion']
    )

    print(objs)
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

    cv2.imshow('Faces: ', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



def get_wikipedia_summary(title):
    # Define the endpoint
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"

    # Send a GET request to the Wikipedia API
    response = requests.get(url)

    # If the request was successful, return the summary and lifespan
    if response.status_code == 200:
        summary = response.json()["extract"]
        description = response.json()["description"]
        # Try to find a lifespan in the summary
        lifespan_match = re.search(r'\((\d{4})\s*–\s*(\d{4})\)', description)
        if lifespan_match:
            birth_year, death_year = lifespan_match.groups()
            lifespan = f"{birth_year} - {death_year}"
        else:
            lifespan = "Lifespan not found in summary."

        return summary, lifespan
    else:
        return None, None


directory = 'Images'
names,pictures = get_names_from_files(directory)
for name in names:
    print(name)
print(f"Nr of pictures: {pictures}" )
print(f"Nr of painters: {len(names)}")

# albert-gleizes_0 - mai abstract;  albin-egger-lienz_20 - 2 persoane
# alphonse-mucha_1 - side profile ; amadeo-de-souza-cardoso_5 - abstract;
# amedeo-modigliani_284 - sketch ; antonio-mancini_4 - veil on face;
# aubrey-beardsley_3 - black and white; boris-kustodiev_70 si boris-kustodiev_69

image_path = 'Images/aubrey-beardsley_3.jpg'
#metadata = get_image_metadata(image_path)
#print(metadata)
objs = get_image_deepface_info(image_path)
print(type(objs))
print(type(objs[0]['region']))
print(objs[0]['region']['x'])

see_faces(image_path, objs)

summary, lifespan = get_wikipedia_summary("Zinaida_Serebriakova")
print(f"Summary: {summary}")
print(f"Lifespan: {lifespan}")



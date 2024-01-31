
import os
import re

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

import json

# Load the original JSON file
with open('portraits.json', 'r') as f:
    data = json.load(f)

# Extract only the desired attributes
extracted_data = [{k: v for k, v in item.items() if k in ["filename", "age", "gender"]} for item in data]

# Write the extracted data to a new JSON file
with open('portraits_training.json', 'w') as f:
    json.dump(extracted_data, f, indent=4)
    

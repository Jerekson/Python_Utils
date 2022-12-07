import json

# read properties.json 
with open('properties.json') as json_file:
    properties = json.load(json_file)

print(properties)
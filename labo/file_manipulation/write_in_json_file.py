import json

with open('properties.json') as json_file:
    properties = json.load(json_file)
    properties["StringProperty"] = "new value"
    json.dump(properties, json_file)
    
print(properties)

"""
with open('data.json', 'r+') as f:
    data = json.load(f)
    data['id'] = 134 # <--- add `id` value.
    f.seek(0)        # <--- should reset file position to the beginning.
    json.dump(data, f, indent=4)
    f.truncate()     # remove remaining part
"""
import json, os
from pathlib import Path

dir_path = Path(__file__).resolve().parent
json_file_path = dir_path / "test_json_module.json"

def get_json_file_data(file_path):
    try:
        content = file_path.read_text(encoding="utf-8")
        data = json.loads(content)
        return data
    except Exception as e:
        print(e)

def set_default_data(file_path):
    default_data = {
        "default datas" : [
            {
                "Author":"moi",
                "year":2025,
                "my file path":str(json_file_path)
            }
        ]
    }
    try:
        file_path.write_text(json.dumps(default_data, indent=4), encoding="utf-8")
        print("file created and default data set")
    except Exception as e:
        print(e)

def add_data(file_path):
    current_data = get_json_file_data(file_path)
    # set new data
    current_data["new data"] = "test"

    # save 
    file_path.write_text(json.dumps(current_data, indent=4), encoding="utf-8")

def delete_data(file_path, data, suppr):
    pass

# check if file exist, if it is, get current data
if json_file_path.exists():
    data = get_json_file_data(json_file_path)
else: # if not, create it and set default data 
    data = set_default_data(json_file_path)

# add datas
data["new data"] = [{
    "skey1":"test",
    "skey2":"Hello"
}]
data["new data2"] = [{
    "skey1":"test2",
    "skey2":"Hello2"
}]
data["new data3"] = [{
    "skey1":"test3",
    "skey2":"Hello3"
}]

# delete some data
delete_data(json_file_path, data, "new data2")

# save new datas
json_file_path.write_text(json.dumps(data, indent=4), encoding="utf-8")


import json, logging, sys, datetime
from pathlib import Path

log = logging.getLogger(__name__)

def create_json_file(json_file_path, file_name):
    log.debug("create_json_file methode started")
    today_date = datetime.datetime.now().strftime("%Y-%m-%d")
    default_data = {
        "metadata" :{
                "Author": "ToDoList_original_creation",
                "file_name": str(file_name),
                "created_date": today_date,
                "description": "TODO : set description"
            }
    }
    try:
        json_file_path.write_text(json.dumps(default_data, indent=4), encoding="utf-8")
        log.debug("file created and default data set")
    except Exception as e:
        log.error(e)

def get_default_json_dir_path():
    log.debug("get_default_json_path start")
    dir_path = Path(__file__).resolve().parent
    return dir_path.parent / "data"

def get_default_json_path_lists():
    log.debug("get_default_json_lists start")
    base_dir = get_default_json_dir_path()
    json_path_list = list(base_dir.glob('*.json'))
    return json_path_list

def read_json_file(json_file_path):
    log.debug("read_json_file start")
    try:
        content = json_file_path.read_text(encoding="utf-8")
        data = json.loads(content)
        return data
    except AttributeError as e:
        log.error(f"Attribute error for file \n{json_file_path}")
        raise e
    except FileNotFoundError as e:
        log.error("File not Found")
        raise e
    except json.decoder.JSONDecodeError as e:
        log.error(f"file cannot be decoded \n{json_file_path}\nYou have to select a good one")
        raise e
        

def get_json_file_data(json_file_path):
    log.debug("get_json_file_data start")
    try:
        content = json_file_path.read_text(encoding="utf-8")
        list_data = json.loads(content)
        log.debug(f"list_data : {list_data}")
        all_datas = []
        for data in list_data:
            log.debug(f"data : {data}")
            if data.startswith("task_"):
                log.debug(f"data value name {list_data[data]['name']}")
                all_datas.append([list_data[data]["name"],
                                  list_data[data]["description"],
                                  list_data[data]["estimated_duration"],
                                  list_data[data]["status"]
                                ])
        return all_datas
    except Exception as e:
        log.error(e)

def file_exists(file):
    log.debug(f"file_exists started for file {file}")

def add_new_task(json_file_path, task_infos):
    log.debug("add_new_task function start")
    data = read_json_file(json_file_path)
    data["task_"+task_infos["name"]] = {
        "name":task_infos["name"],
        "description":task_infos["description"],
        "estimated_duration":task_infos["estimated_duration"],
        "status":"todo"
    }
    # save new datas
    json_file_path.write_text(json.dumps(data, indent=4), encoding="utf-8")
    log.info(task_infos)

def change_status():
    log.debug("change_status function start")

def get_specific_task():
    log.debug("get_specific_task function start")

def extract_json_file():
    log.debug("extract_json_file function start")


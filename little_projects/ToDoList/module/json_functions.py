import json, logging
from pathlib import Path

log = logging.getLogger(__name__)

def set_default_data(json_file_path):
    log.debug("set_default_data start")
    default_data = {
        "metadata" :{
                "Author": "ToDoList_original_creation",
                "file_name": "TODO : set file name",
                "created_date": "TODO : get and set today's date",
                "description": "TODO : set description"
            }
    }
    try:
        json_file_path.write_text(json.dumps(default_data, indent=4), encoding="utf-8")
        log.debug("default data set")
    except Exception as e:
        log.error(e)   

def create_json_file():
    log.debug("create_json_file methode started")

def get_default_json_dir_path():
    log.debug("get_default_json_path start")
    dir_path = Path(__file__).resolve().parent
    return dir_path.parent / "data"

def get_default_json_path_lists():
    log.debug("get_default_json_lists start")
    base_dir = get_default_json_dir_path()
    json_path_list = list(base_dir.glob('*.json'))
    return json_path_list

def get_json_file_data(json_file_path):
    log.debug("get_json_file start")
    try:
        content = json_file_path.read_text(encoding="utf-8")
        data = json.loads(content)
        return data
    except FileNotFoundError as e:
        log.error("File not Found")
    except json.decoder.JSONDecodeError as e:
        log.error(f"file cannot be decoded \n{json_file_path}")

def file_exists(file):
    log.debug(f"file_exists started for file {file}")

def add_new_task():
    log.debug("add_new_task function start")

def change_status():
    log.debug("change_status function start")

def get_specific_task():
    log.debug("get_specific_task function start")

def extract_json_file():
    log.debug("extract_json_file function start")


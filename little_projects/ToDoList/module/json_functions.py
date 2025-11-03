import json, logging
from pathlib import Path

log = logging.getLogger(__name__)

dir_path = Path(__file__).resolve().parent
json_file_path = dir_path.parent / "data/tasks_save.json"

def create_json_file():
    log.debug("create_json_file methode started")

def file_exists(file = json_file_path):
    log.debug(f"file_exists started for file {file}")
    isfile = Path(file).is_file()
    if isfile:
        return isfile
    elif file == json_file_path:
        return "file don't exists, but can be create automatically"
    else:
        return "Ohlolo it will be relou"


def add_new_task():
    log.debug("add_new_task function start")

def change_status():
    log.debug("change_status function start")

def get_task():
    log.debug("get_task function start")

def get_all_tasks():
    log.debug("get_all_tasks function start")


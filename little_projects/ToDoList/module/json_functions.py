import json, logging
from pathlib import Path

log = logging.getLogger(__name__)



def create_json_file():
    log.debug("create_json_file methode started")

def get_default_json_path():
    log.debug("get_default_json_path start")
    dir_path = Path(__file__).resolve().parent
    return dir_path.parent / "data"

def get_default_json_path_lists():
    log.debug("get_default_json_lists start")
    base_dir = get_default_json_path()
    json_path_list = list(base_dir.glob('*.json'))
    return json_path_list

def file_exists(file):
    log.debug(f"file_exists started for file {file}")
    isfile = Path(file).is_file()
    if isfile:
        return isfile
    else:
        return "file not found"


def add_new_task():
    log.debug("add_new_task function start")

def change_status():
    log.debug("change_status function start")

def get_task():
    log.debug("get_task function start")

def get_all_tasks():
    log.debug("get_all_tasks function start")


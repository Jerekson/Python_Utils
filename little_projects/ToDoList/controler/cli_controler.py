import logging, sys
from ..module import utils, json_functions as json
from ..view import cli_view

log = logging.getLogger(__name__)

def add_new_task():
    log.debug("add_new_task start")
    # Ask users task's details 
    new_task = cli_view.add_task()
    print(new_task)

    

def task_done():
    log.debug("task_done start")

def update_task():
    log.debug("update_task start")

def show_tasks():
    log.debug("show_tasks start")

def show_specific_task():
    log.debug("show_specific_task start")

def cli_controler_run():
    log.debug("cli_controler start")
    
    # Get json file list
    json_list = json.get_default_json_path_lists()
    print(len(json_list))
    json_select_index = cli_view.get_json_file(json_list)
    print(json_list[json_select_index])
    sys.exit()

    # task selection
    result = cli_view.main_menu()
    # Dictionary linking the option index to the corresponding function for tasks actions
    actions = {
    0: add_new_task,
    1: task_done,
    2: update_task,
    3: show_tasks,
    4: show_specific_task,
    5: lambda: sys.exit() # Use a lambda to exit the application correctly
    }
    if result in actions:
        log.debug("result in action True")
        actions[result]()


    
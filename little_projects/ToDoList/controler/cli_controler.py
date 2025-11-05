import logging, sys
from ..module import utils, json_functions as json
from ..view import cli_view
from pathlib import Path

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

def get_json_file_run():
    log.debug("get_json_list start")
    # Get json file list
    json_default_list = json.get_default_json_path_lists()
    other_options = [
        "create new task list",
        "Select an other specific task list (json file only)"
    ]

    json_select_index = cli_view.select_json_file(json_default_list, other_options)

    # if the index is in the default json list
    if json_select_index < len(json_default_list):
        return Path(json_default_list[json_select_index])
    else:
        # if its new, then create it.
        specific_select = other_options[json_select_index - len(json_default_list)]
        log.debug(f"Specific selection -> {specific_select}")
        if specific_select == "create new task list":
            response = cli_view.prepare_json_file_path()
            log.debug(f"the new task list file is : {response}")
            if response[0]:
                default_dir = json.get_default_json_dir_path()
                json_file_path = Path(default_dir) / Path(response[1])
                if json_file_path.is_file():
                    log.error("file already exists")
                    retry()
                json.create_json_file(json_file_path, response[1])
                return json_file_path
            else:
                json_file_path = Path(response[2]) / Path(response[1])
                if json_file_path.is_file():
                    log.error("file already exists")
                    retry()
                json.create_json_file(json_file_path, response[1])
                return json_file_path
        elif specific_select == "Select an other specific task list (json file only)":
            while True:
                json_file_path = Path(cli_view.select_specific_json_file_path())
                if json_file_path.is_file() and json_file_path.suffix.lower() == ".json":
                    return json_file_path
                else:
                    print("File Not Found")

def check_json_file_origin(json_file_data):
    log.debug("check_json_file_origin start")
    try: 
        if json_file_data["metadata"]["Author"] == "ToDoList_original_creation":
            return True
        else:
            return False
    except KeyError as e:
        log.debug(f"Dont find 'metadata'\n{e}")
    except Exception as e:
        log.error(type(e))

def select_task_action():
    log.debug("select_task_action start")
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

def retry():
    try:
        response = input("Would you retry ? (yes) / (no)\n")
        if response == "yes" or response == "y":
            cli_controler_run()
        else:
            sys.exit()
    except Exception as e:
        log.error(type(e))

def cli_controler_run():
    log.debug("cli_controler start")

    try:
        json_file = get_json_file_run()
        json_file_data = json.get_json_file_data(json_file)

        # first, check if the json file was created by this program. 
        # If not, prevent the user
        if not check_json_file_origin(json_file_data):
            log.info("file not created by this ToDoList program")
            response = input("Do you still want to use this file ? (yes) / (no) \n")
            if response == "yes" or response == "y":
                log.warning("You have selected (yes)")
            else:
                retry() 
    except (EOFError,KeyboardInterrupt, AssertionError, TypeError):
        sys.exit(0) 
    except AttributeError as e:
        log.error(e)
        sys.exit()
    except Exception as e:
        log.debug(type(e))
        retry()
    
    select_task_action()
    

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
    else: # TODO : One of other_options
        # if its new, then create it.
        specific_select = other_options[json_select_index - len(json_default_list)]

        # if its a specific file, check if it's a file created by this program. If not
        # prevent the user that this program it's not responsible of the alteration of the next 
        # json file. a ask the user if it's really ok for that. 
    return 'TODO : return the file'

def check_json_file_origin(json_file_data):
    log.debug("check_json_file_origin start")
    try: 
        # TODO : read the file to see the entete
        return True
    except Exception as e:
        log.error(e)

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

def cli_controler_run():
    log.debug("cli_controler start")
    
    json_file = get_json_file_run()
    json_file_data = json.get_json_file_data(json_file)

    
    sys.exit()

    # first, check if the json file was created by this program. 
    # If not, prevent the user
    # print(json_file_data["metadata"]["Author"])
    if check_json_file_origin(json_file_data):
        log.info("this file is good")
    else:
        log.info("file not created by this ToDoList program")
        response = input("Do you still want to use this file ?\n")       
    sys.exit()
    select_task_action()


'''
1 - je récupère le json file. bêtement. 
2 - Je vérifie s'il est à moi. 
3 - si c'est le cas. Je passe au point 4. 
3.5 - Si ce n'est pas le cas. Je demande si je peux vraiment l'utiliser. 
4 - Je pose mes questions. 
'''


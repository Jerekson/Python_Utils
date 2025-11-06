# litlle_projects.ToDoList.utils.utils
import logging, os
from pathlib import Path

log = logging.getLogger(__name__)


def validation_str_value(value, type=""):
    log.debug(f"validation_str_value methode for value '{value}' started")
    if type == "name" and value == "":
        raise ValueError("Ce champ ne peut pas être vide.")

    # TODO : Preventing injection and json injection 
    return value

def validation_int_value(value, type=""):
    log.debug(f"validation_int_value methode for value '{value}' started")
    try:
        value_int = int(value.strip() or "0")
        return value_int
    except ValueError:
        if type == "TED":
            raise ValueError("Nothing or a number was expected for the input field 'estimated duration in minute'")
        else:
            raise ValueError("Not and integer entered")

def control_json_filename(filename):
    log.debug("control_json_filename start")
    invalid_cara = [',',';','/','\\', '&', '|', '!', '`', '$', '(', ')','*','{','[','`','^','}','£','¨','%','µ','§',':','?',']','}']
    try:
        # First control
        if any(c in filename for c in invalid_cara):
            print(f"One of these invalid caractere was entered \n{invalid_cara}")
            return False
        # control file lenght
        if len(filename) < 3:
            print("The task list must have at least 3 caracteres")
            return False
        return True
    except Exception as e:
        log.error(type(e))


def control_dir_path_entry(dir_path):
    log.debug("contro_dir_path start")
    dir_path = Path(dir_path)
    try:
        # is dir exists ? 
        if dir_path.is_dir():
            print(dir_path.resolve())
        else:
            print(f"The path '{dir_path}' is invalid")
            return False
            
        #Does the user have the right to read and write in this dir ? 
        if os.access(dir_path, os.R_OK) and os.access(dir_path, os.W_OK):
            return True
        else:
            print("You have no right to read and/or write in this directory")
            return False
        
    except Exception as e:
        raise e

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
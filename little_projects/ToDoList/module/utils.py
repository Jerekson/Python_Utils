# litlle_projects.ToDoList.utils.utils
import logging

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
    return True
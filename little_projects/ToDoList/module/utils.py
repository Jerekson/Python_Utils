# litlle_projects.ToDoList.utils.utils
import logging

log = logging.getLogger(__name__)

def validation_str_value(value, type=""):
    log.debug(f"validation_str_value methode for value '{value}' started")
    if type == "name" and value == "":
        raise ValueError("Ce champ ne peut pas être vide.")

    # TODO : Preventing injection and json injection 
    return value
import logging
from ..module import utils
from ..view import cli_view

log = logging.getLogger(__name__)

def cli_controler_run():
    log.debug("cli_controler start")
    result = cli_view.simple_select_menu()
    

'''

if result == "show all tasks":
    pass

elif result == "show a specific task":
    pass

elif result == "add a new task":
    new_task_name = input("set a new task name")
    print(new_task_name)

elif result == "update task":
    pass

elif result == "task done":
    pass

elif result == "quit":
    sys.exit()
'''
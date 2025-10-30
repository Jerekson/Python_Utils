import logging, argparse, sys
from .utils.logging_config import logging_setup
from .todolist import Todolist
from .utils import utils

def parser():
    parser = argparse.ArgumentParser(description="""To Do List""")

    parser.add_argument("-mode-ihm", dest="ihm", action="store_true", help="start IHM mode", required=False)
    parser.add_argument("-v", action="store_true", help="Mode verbose")

    return parser.parse_args()

    

def main():
    # retrieve args
    args = parser()

    # Log configuration
    if args.v:
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO

    logging_setup(level=log_level)
    log = logging.getLogger("little_projects.ToDoList")
    log.debug("main log configured and start with theses args \n%s", args)

    if args.ihm:
        log.debug("mode IHM started")
    else:
        log.debug("mode console started")
        result = utils.simple_select_menu()
        if result == "show all tasks":
            Todolist.get_tasks()
        elif result == "show a specific task":
            Todolist.get_specific_task()
        elif result == "add a new task":
            Todolist.add_task()
        elif result == "update task":
            Todolist.update_task()
        elif result == "task done":
            Todolist.task_done()
        elif result == "delete task":
            Todolist.delete_task()
        elif result == "quit":
            sys.exit()


if __name__ == "__main__":
    main()
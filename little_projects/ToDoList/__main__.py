import logging, argparse, sys
from .utils.logging_config import logging_setup
from .todolist import *
from .utils import utils
from .task import Task

def parser():
    parser = argparse.ArgumentParser(description="""To Do List""")

    parser.add_argument("--gui", dest="gui", action="store_true", help="start IHM mode")
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

    if args.gui:
        log.debug("mode IHM started")
    else:
        log.debug("mode console started")
        result = utils.simple_select_menu()
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

        # Si je veux créer une tâche, là je créer un nouvel objet. 
        # Si je veux modifier une tâche, je créer un objet et je récupère ses valeurs

        # Si je veux supprimer une tâche, je supprimer simplement la ligne


if __name__ == "__main__":
    main()
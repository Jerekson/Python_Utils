import logging, argparse
from .utils.logging_config import logging_setup
from .todolist import Todolist

def parser():
    parser = argparse.ArgumentParser(description="To Do List")

    parser.add_argument("-show", dest="show", action="store_true", help="print all tasks", required=False)
    parser.add_argument("-show_spe", dest="show_spe", help="print specific type of tasks", required=False)
    parser.add_argument("-add", dest="add_task", action="store_true", help="add new task", required=False)
    parser.add_argument("-delete", dest="delete_task", help="delete task", required=False)
    parser.add_argument("-update", dest="update_task", help="update a task", required=False)
    parser.add_argument("-done", dest="task_done", help="task done", action="store_true", required=False)

    parser.add_argument("-v", action="store_true", help="Mode verbose")
    return parser.parse_args()

    

def main():
    print("main start")

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

    # Start
    Todolist().add_task()

if __name__ == "__main__":
    main()
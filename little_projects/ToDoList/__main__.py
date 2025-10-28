import logging, argparse, sys
from .utils.logging_config import logging_setup
from .todolist import Todolist
from .utils import utils

def parser():
    parser = argparse.ArgumentParser(description="""To Do List \n
        You have to enter at least one argument. \n
        By default, if nothing is entered, a small menu will appear""")

    parser.add_argument("-show", dest="show", action="store_true", help="print all tasks", required=False)
    parser.add_argument("-show_spe", dest="show_spe", action="store_true", help="print specific type of tasks", required=False)
    parser.add_argument("-add", dest="add_task", action="store_true", help="add new task", required=False)
    parser.add_argument("-delete", dest="delete_task", action="store_true", help="delete task", required=False)
    parser.add_argument("-update", dest="update_task", action="store_true", help="update a task", required=False)
    parser.add_argument("-done", dest="task_done", help="task done", action="store_true", required=False)

    parser.add_argument("-v", action="store_true", help="Mode verbose")
    return parser.parse_args()

    

def main():
    print("main start")

    # retrieve args
    args = parser()

    # get number of element set 
    argv_numb = len(sys.argv)
    print(argv_numb)

    # Log configuration
    if args.v:
        log_level = logging.DEBUG
        argv_numb = argv_numb - 1
    else:
        log_level = logging.INFO

    logging_setup(level=log_level)
    log = logging.getLogger("little_projects.ToDoList")
    log.debug("main log configured and start with theses args \n%s", args)

    if(argv_numb > 2):
        print("You have to set at least one argument, enter -h or -help for help")
        log.info("the user has entered too many arguments %s", argv_numb)
        sys.exit()

    log.info("test")

    

if __name__ == "__main__":
    main()
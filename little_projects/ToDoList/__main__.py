import logging, argparse
from .utils.logging_config import *
from . import todolist

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
    # retrieve args
    args = parser()
    
    # Log configuration

    # Start

if __name__ == "__main__":
    main()
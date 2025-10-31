import logging, argparse, sys
from .module.logging_config import logging_setup
from .controler import cli_controler, gui_controler

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
        cli_controler.cli_controler_run()

if __name__ == "__main__":
    main()
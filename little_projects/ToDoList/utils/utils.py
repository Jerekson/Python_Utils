# litlle_projects.ToDoList.utils.utils
import logging

log = logging.getLogger(__name__)

def show_menu():
	log.debug("show_menu function start")
	# Setting options
	options = {
	1: "show all tasks",
	2: "show specific task",
	3: "add new task",
	4: "update task",
	5: "task done ",
	6: "quit"
	}

	# Top border
	print("\n" + "-" * 35)
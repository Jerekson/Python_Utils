import logging
from simple_term_menu import TerminalMenu

log = logging.getLogger(__name__)

def simple_select_menu():
	log.debug("simple_select_menu function start")
	options = [
	"show all tasks",
	"show a specific task",
	"add a new task",
	"update task",
	"task done",
	"delete task",
	"quit"
	]
	terminal_menu = TerminalMenu(options)
	menu_entry_index = terminal_menu.show()
	return options[menu_entry_index]
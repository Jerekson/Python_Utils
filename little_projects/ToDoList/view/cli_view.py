import logging, sys
from simple_term_menu import TerminalMenu
from ..module import utils

log = logging.getLogger(__name__)

def main_menu():
	log.debug("main_menu function start")
	# Set options 
	options = [
	"add a new task",
	"task done",
	"update task",
	"show all tasks",
	"show a specific task",
	"quit"
	]

	# create the view 
	terminal_menu = TerminalMenu(
		options,
		title="=== TO DO list ===",
        menu_cursor="-> ",
        menu_cursor_style=("fg_blue", "bold"),
        menu_highlight_style=("bg_gray", "fg_blue"),
		)

	# print the view and get the choice
	menu_entry_index = terminal_menu.show()

	# actions based on the entry 
	if menu_entry_index is None: 
		# if the user enter Ctrl+C or Ctrl+D
		print("\nForced exit.")
		sys.exit(0)
	return menu_entry_index

def add_task():
	log.debug("add_task start")
	print("Add new task selected")
	while True:
		try:
			task_name = utils.validation_str_value(input("task name : "), "name")
			task_description = utils.validation_str_value(input("description (facultative) : "))

			task_estimated_duration = int(input("estimated duration in minute (facultative) : ").strip() or "0")
		except ValueError as e:
			print(e)
			continue
		# TODO : create specific value error
		#print("An incorrect value has been entered, an integer is expected")

		return {
		"name": task_name,
		"description": task_description,
		"estimated_duration": task_estimated_duration
		} 
		
	print(task)
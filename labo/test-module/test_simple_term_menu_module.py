from simple_term_menu import TerminalMenu
import os


def simple_select_menu():
	options = [
	"Entry 1",
	"Entry 2",
	"Entry 3"
	]
	terminal_menu = TerminalMenu(options)
	menu_entry_index = terminal_menu.show()
	print(f"You have selected {options[menu_entry_index]} ?")

def multiple_select_menu():
	terminal_menu = TerminalMenu([
		"Entry 1",
		"Entry 2",
		"Entry 3",
		"Entry 4"
		],
		multi_select = True,
		show_multi_select_hint = True
	)
	menu_entry_indices = terminal_menu.show()
	print(menu_entry_indices)
	print(terminal_menu.chosen_menu_entries)

def list_files(directory="."):
	return (file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file)))

def preview_files():
	terminal_menu = TerminalMenu(list_files(), preview_command="bat --color=always {}", preview_size=0.75)
	menu_entry_index = terminal_menu.show()


if __name__ == "__main__":
	# simple_select_menu()
	multiple_select_menu()
	# preview_files()
	pass
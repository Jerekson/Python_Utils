from simple_term_menu import TerminalMenu


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
	pass

if __name__ == "__main__":
	simple_select_menu()
	multiple_select_menu()
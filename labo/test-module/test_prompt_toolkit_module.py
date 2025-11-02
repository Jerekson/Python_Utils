from prompt_toolkit import prompt

def simple_prompt():
	answer = prompt("set an input : ")
	print("the enter : %s"% answer)

def prompt_session_uses():
	from prompt_toolkit import PromptSession 
	session = PromptSession()
	text1 = session.prompt('first enter : ')
	text2 = session.prompt("second enter : ")
	print(text1)

def auto_completion():
	from prompt_toolkit.completion import WordCompleter

	html_completer = WordCompleter([
		"<html>",
		"<body>",
		"<head>",
		"<title>"
		])
	text = prompt("Enter html: ", completer=html_completer)

def input_validation():
	pass

if __name__ == "__main__":
	# simple_prompt()
	# prompt_session_uses()
	auto_completion()
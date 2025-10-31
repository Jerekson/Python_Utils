import logging


result = utils.simple_select_menu()
if result == "show all tasks":
    pass

elif result == "show a specific task":
    pass

elif result == "add a new task":
    new_task_name = input("set a new task name")
    print(new_task_name)

elif result == "update task":
    pass

elif result == "task done":
    pass

elif result == "quit":
    sys.exit()
# 1 - add tasks to a list
# 2 - mark tasks as done
# 3 - view all tasks
# 4 - Quit the program

Message = """
Welcome to the Task Manager!
1 - Add a task
2 - Mark a task as done
3 - View all tasks
4 - Quit the program
"""
tasks = []
def add_task():
    pass
def view_tasks():
    ...
def mark_task_as_done():
    pass

while True:
    print(Message)
    input_value = input("Please select an option (1-4): ").strip()
    if input_value == "1":
        add_task()
    elif input_value == "2":
        mark_task_as_done()
    elif input_value == "3":
        view_tasks()
    elif input_value == "4":
        print("Exiting the Task Manager. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")


    
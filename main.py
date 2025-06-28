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

def add_task():
    # get task from user
    task = input("Enter the task you want to add: ").strip()
    # define task status
    task_info = { "task" : task, "done": False }
    # add task to the list
    tasks.append(task_info)
    print("Task dded successfully.")

def mark_task_as_done():
    # get list of incomplete tasks
    incomplete_tasks = [task for task in tasks if task["done"] == False]
    # check if there are no incomplete tasks
    if not incomplete_tasks:
        print("No incomplete tasks found.")
        return
    # show them to the user
    for index, task in enumerate(incomplete_tasks):
        print(f"{index + 1}. {task['task']}")
        print("-" * 20 )
    # ask user to select a task to mark as done
    task_number = input("Enter the number of the task you want to mark as done: ").strip()
    # check if the task number is valid
    if task_number.isdigit() and 1 <= int(task_number) <= len(incomplete_tasks):
        task_index = int(task_number) - 1
        tasks[tasks.index(incomplete_tasks[task_index])]["done"] = True
        print("Task marked as done successfully.")
    else:
        print("Invalid task number. Please try again.")
    
    
def view_tasks():
    # check if there are no tasks
    if not tasks:
        print("No tasks found.")
        return
    # show all taks
    for index, task in enumerate(tasks):
        status = "✔" if task["done"] else "✘"
        print(f"{index + 1} - {task['task']} [{status}]")
    
    
        
tasks = []
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


    
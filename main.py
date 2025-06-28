# 1 - add tasks to a list
# 2 - mark tasks as done
# 3 - view all tasks
# 4 - Quit the program




tasks = [{"task":"Quran", "done":True}, {"task":"Salah", "done":True}, 
         {"task":"Study", "done":False}, {"task":"Exercise", "done":True}, 
         {"task":"Sleep", "done":False}, {"task":"Visit Hamada", "done":True}]

def main():
    Message = """
        Welcome to the Task Manager!
        1 - Add a task
        2 - Mark a task as done
        3 - View all tasks
        4 - Quit the program
    """
    while True:
        print(Message)
        input_value = input("Please select an option (1-4): ").strip()
        if input_value == "1":
            add_task()
        elif input_value == "2":
            mark_task_as_done()
        elif input_value == "3":
            view_tasks(tasks)
        elif input_value == "4":
            print("Exiting the Task Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

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
    try:
        # ask user to select a task to mark as done 
        task_number = int(input("Enter the number of the task you want to mark as done: ").strip())
        # check if the task number is valid
        while task_number < 1 or task_number > len(incomplete_tasks):
            print("Invalid task number. Please try again.")
            task_number = int(input("Enter the number of the task you want to mark as done: ").strip())
        
        tasks[tasks.index(incomplete_tasks[task_number - 1])]['done'] = True
        print("Task marked as done successfully.")
    except ValueError:
        print("Invalid task number. Please try again.")
    

    
    
def view_tasks(P_tasks):
    # check if there are no tasks
    if not P_tasks:
        print("No tasks found.")
        return
    # show all taks
    for index, task in enumerate(P_tasks):
        status = "✔" if task['done'] else "✘"
        print(f"{index + 1} - {task['task']} [{status}]")

if __name__ == "__main__":
    main()
        



    
print("---TO-DO LIST APP---")
print(".....Welcome on Board🤗 .....")

menu =(" What would you like to do? \n 1. Add task \n 2. View Task \n 3.Delete/ Markdone \n 4.Exit")
user_input = input("Choose from the menu (1-4): ")


def load_task(tasks):
    tasks = []
    try: 
        with open("task.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        task = []
        return tasks

def add_task(tasks):
    new_task = input("Enter task name: ")
    tasks.append(new_task)

    with open("tasks.txt", "a") as file:
        file.write(new_task + "\n")
        print("Task added Successfully!")


def view_tasks(tasks):
    print("\n Your Task: ")
    try:
        with open("tasks.txt", "r") as file:
            lines = file.readline()
            if not lines:
                print("Not task yet!")
            else:
                for i, task in  enumerate(lines, start = 1):
                    print(f"{i}.{task.strip()}")
                    print("All viewed ✔✔")
    except FileNotFoundError:
        print("No task file found, add in task to view.")


def delete_task(tasks):
    try:
        task_delete = int(input("Input task number to be deleted: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No task yet")
                return
            
            for i, task in enumerate(tasks, start = 1):
                print(f"{i}.{task.strip()}")
                task_num = input("Enter the number of task to delete: ")
                if not task_num.isdigit() or int(task_num) < 1 or int(task_num) > len(tasks):
                    print("Invalid task number")
                    return
                
                deleted_task = tasks.pop(int(task_num) -1)
            with open("task.txt", "w") as file:
                file.writelines(task)
                print(f"Task'{deleted_task.strip()}' deleted succesfully ✔")
    except FileNotFoundError:
        print("No task file found yet, Please add task first!")



def mark_task_done(tasks):
    if not task:
        print("No tasks marked done.")
        return
    
    print("\n Your current task")
    for i, task in enumerate(tasks, start = 1):
                print(f"{i}.{tasks}")

    task_done = input("Input task number completed: ")
    if not task_done.isdigit():
        print("Please enter a number!")
        return
    
    task_done = int(task_num)
    if task_done < 1 or task_done > len(tasks):
        print("Number not found in task")
        return
    
    completed_task = tasks[task_done -1]
    tasks[task_done -1] = completed_task "✔"

    print(f"Task '{completed_task}' marked as done!")

    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    return tasks





    
     







    

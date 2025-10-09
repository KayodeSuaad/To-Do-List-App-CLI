def load_task():
    tasks = []
    try: 
        with open("tasks.txt", "r", encoding = "utf-8") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        tasks = []
    return tasks

def add_task(tasks):
    new_task = input("Enter task name: ")
    tasks.append(new_task)

    with open("tasks.txt", "a", encoding = "utf-8") as file:
        
        file.write(new_task + "\n")
        print("Task added Successfully!")


def view_task(tasks):
    print("\n Your Task: ")
    try:
        with open("tasks.txt", "r", encoding = "utf-8") as file:
            lines = file.readlines()
            if not lines:
                print("Not task yet!")
            else:
                for i, task in  enumerate(lines, start = 1):
                    print(f"{i}.{task.strip()}")

                print("Viewing Task in process....")
    except FileNotFoundError:
        print("No task file found, add in task to view.")


def delete_task(tasks):
    try:
        task_delete = int(input("Input task number to be deleted: "))
        with open("tasks.txt", "r" , encoding = "utf-8") as file:
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
            with open("tasks.txt", "w") as file:
                file.writelines(task)
                print(f"Task '{deleted_task.strip()}' deleted succesfully ✔")
    except FileNotFoundError:
        print("No task file found yet, Please add task first!")



def mark_task_done(tasks):
    if not tasks:
        print("No tasks marked done.")
        return
    print("\n Your current task")

    for i, task in enumerate(tasks, start = 1):
                print(f"{i}.{task}")

    task_done = input("Input task number completed: ")
    if not task_done.isdigit():
        print("Please enter a number!")
        return
    
    task_done = int(task_done)
    if task_done < 1 or task_done > len(tasks):
        print("Number not found in task")
        return
    
    completed_task = tasks[task_done -1]
    tasks[task_done -1] = completed_task +  "✔"

    print(f"Task '{completed_task}' marked as done!")

    with open("tasks.txt", "w", encoding = "utf-8") as file:
        for task in tasks:
            file.write(task + "\n")
    return tasks



while True:
    tasks = load_task()

    print("---TO-DO LIST APP---")
    print(".....Welcome on Board🤗 .....")

    print(" What would you like to do? \n 1. Add task \n 2. View Task \n 3.Delete \n 4.Markdone \n 5.Exit")
    user_input = input("Choose from the menu (1-5): ")

    if user_input == "1":
        add_task(tasks)
    elif user_input =="2":
        view_task(tasks)
    elif user_input =="3":
        delete_task(tasks)
    elif user_input == "4":
        mark_task_done(tasks)
    elif user_input =="5":
        print("Goodbye!!! 🤞")
        break
    else:
        print("Incorrect number, Choose between 1-5")







    
     







    

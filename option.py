print("---TO-DO LIST APP---")
print(".....Welcome on Board🤗 .....")

menu =(" What would you like to do? \n 1. Add task \n 2. View Task \n 3.Delete/ Markdone \n 4.Exit")
user_input = input("Choose from the menu (1-4): ")

tasks = []

def load_task(tasks):
    pass

def add_task(tasks):
    new_task = input("Enter task name: ")   
    with open("tasks.txt", "a"):
        print("Task added!")
    return tasks.txt


def view_tasks(tasks):
    with open("tasks.txt"):
        if tasks.list == None:
            print("Not task yet!")
        elif tasks.list == True:
            for i, task in  enumerate(tasks, start = 1):
                print(f"{1}.{task}")
            print("All viewed ✔✔")


def delete_task(tasks):
    print(tasks)
    task_delete = input("Input task number to be deleted: ")
    with open("tasks.txt"):
        for i, task in enumerate(tasks, start = 1):
            if i == task_delete:
                tasks = [-1]
                print("Task deleted succssfully..")
    return tasks

        

def mark_task_done(tasks):
    task_done = input("Input task number completed: ")
    with open("tasks.txt"):
        for i, task in enumerate(tasks, start = 1):
            if task_done == tasks:
                print(f"{i}.{tasks}✔")

    print(tasks)


    
     







    

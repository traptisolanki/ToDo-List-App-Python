tasks = []

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip()) 

    except FileNotFoundError:
        pass

def save_tasks():
    with open("tasks.txt", "w") as file:
        # tasks.txt naam ki file open karte hai
        for task in tasks:
            file.write(task + "\n")
            # har task ko file mein save karte hai

def add_task():
    task = input("Enter Task: ")
    tasks.append(task)
    save_tasks()
    print("Task Added Successfully! ")

def view_tasks():
    if len(tasks) == 0:
        print("No Tasks Available!")
    else:
        print("\nTasks List:")
        for task in tasks:
            print(task)

def delete_task():
    task = input("Enter Task to Delete: ")

    if task in tasks:
        tasks.remove(task)
        save_tasks()
        print("Task Deleted Successfully!")
    else:
        print("Task Not Found!")
load_tasks()

while True:
    print("\n===== TO-DO LIST APP =====")
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        print("Program Closed")
        break

    else:
        print("Invalid Choice!")
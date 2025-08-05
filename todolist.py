# Simple To-Do List Manager

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def main():
    tasks = load_tasks()
    while True:
        print("\nYour Tasks:", tasks)
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter new task: ")
            tasks.append(task)
            save_tasks(tasks)
        elif choice == "2":
            task = input("Enter task to remove: ")
            if task in tasks:
                tasks.remove(task)
                save_tasks(tasks)
            else:
                print("Task not found!")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

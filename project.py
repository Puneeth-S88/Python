import os

FILE = "tasks.txt"

# Load tasks
def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return f.read().splitlines()

# Save tasks
def save_tasks(tasks):
    with open(FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# Show tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found!")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

# Main program
tasks = load_tasks()

while True:
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        view_tasks(tasks)

    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        save_tasks(tasks)
        print("✅ Task added!")

    elif choice == "3":
        view_tasks(tasks)
        try:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                save_tasks(tasks)
                print(f"❌ Removed: {removed}")
            else:
                print("Invalid number!")
        except:
            print("Enter a valid number!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
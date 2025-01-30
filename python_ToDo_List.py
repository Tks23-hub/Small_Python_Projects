

tasks = []

# Display tasks
def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks):
            status = "[x]" if task['done'] else "[ ]"
            print(f"{i + 1}. {status} {task['title']}")

# Add a task
def add_task(title):
    tasks.append({"title": title, "done": False})
    print(f"Task '{title}' added.")

# Mark task as complete
def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]['done'] = True
        print(f"Task '{tasks[index]['title']}' marked as complete.")
    else:
        print("Invalid task number.")

# Delete a task

def delete_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Task '{removed['title']}' deleted.")
    else:
        print("Invalid task number.")

# Main loop
def main():
    while True:
        print("\n--- To-Do List ---")
        show_tasks()
        print("\nOptions:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            add_task(title)
        elif choice == '2':
            show_tasks()
            index = int(input("Enter task number to complete: ")) - 1
            complete_task(index)
        elif choice == '3':
            show_tasks()
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(index)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

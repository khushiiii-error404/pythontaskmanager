tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks available.")
        return
    print("\n--- Task List ---")
    for task in tasks:
        status = "✔ Completed" if task['completed'] else "❌ Not Completed"
        print(f"{task['id']}. {task['title']} [{status}]")

def add_tasks():
    num_tasks = int(input("How many tasks do you want to add? "))
    start_id = len(tasks) + 1
    for i in range(num_tasks):
        title = input(f"Enter title for task {start_id + i}: ")
        tasks.append({'id': start_id + i, 'title': title, 'completed': False})
    print(f"{num_tasks} task(s) added successfully!")

def mark_task_completed():
    if not tasks:
        print("No tasks to mark as completed.")
        return
    show_tasks()
    while True:
        # Check if all tasks are completed, then break automatically
        if all(task['completed'] for task in tasks):
            print("All tasks are completed!")
            break

        try:
            completed_id = int(input("Enter the task ID you want to mark as completed (0 to stop): "))
            if completed_id == 0:
                print("Stopping task completion marking.")
                break
            for task in tasks:
                if task['id'] == completed_id:
                    if task['completed']:
                        print(f"Task '{task['title']}' is already completed.")
                    else:
                        task['completed'] = True
                        print(f"Task '{task['title']}' marked as completed!")
                    break
            else:
                print("Task ID not found. Try again.")
        except ValueError:
            print("Please enter a valid number.")

def edit_task():
    if not tasks:
        print("No tasks to edit.")
        return
    show_tasks()
    while True:
        try:
            edit_id = int(input("Enter the task ID you want to edit (0 to stop): "))
            if edit_id == 0:
                break
            for task in tasks:
                if task['id'] == edit_id:
                    new_title = input(f"Enter new title for task '{task['title']}': ")
                    task['title'] = new_title
                    print(f"Task ID {edit_id} updated to '{new_title}'")
                    break
            else:
                print("Task ID not found. Try again.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task():
    if not tasks:
        print("No tasks to delete.")
        return
    show_tasks()
    while True:
        try:
            delete_id = int(input("Enter the task ID you want to delete (0 to stop): "))
            if delete_id == 0:
                break
            for task in tasks:
                if task['id'] == delete_id:
                    tasks.remove(task)
                    print(f"Task ID {delete_id} deleted!")
                    # Reassign IDs
                    for index, t in enumerate(tasks):
                        t['id'] = index + 1
                    break
            else:
                print("Task ID not found. Try again.")
        except ValueError:
            print("Please enter a valid number.")

def main_menu():
    while True:
        print("\n--- Task Manager Menu ---")
        print("1. Add Tasks")
        print("2. Show Tasks")
        print("3. Mark Task as Completed")
        print("4. Edit Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_tasks()
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            mark_task_completed()
        elif choice == '4':
            edit_task()
        elif choice == '5':
            delete_task()
        elif choice == '6':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main_menu()

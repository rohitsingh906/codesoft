# Define a task class (optional)
class Task:
  def __init__(self, description):
    self.description = description
    self.done = False

# Create a list to store tasks
tasks = []

# Main loop for user interaction
while True:
  # Display menu options
  print("1. Add Task")
  print("2. View Tasks")
  print("3. Mark Task Done")
  print("4. Delete Task (Optional)")
  print("5. Exit")

  # Get user choice
  choice = input("Enter your choice (1-5): ")

  # Handle user selection
  if choice == '1':
    description = input("Enter task description: ")
    # Add task (consider using the Task class)
    tasks.append(description)
  elif choice == '2':
    # Display all tasks with status (done/pending)
    if tasks:
      for i, task in enumerate(tasks):
        print(f"{i+1}. {task} ({'Done' if task.done else 'Pending'})")  # Assuming Task class
    else:
      print("No tasks in the list.")
  elif choice == '3':
    # Get task number to mark done
    if tasks:
      task_num = int(input("Enter task number to mark done (1-{}: ".format(len(tasks)))) - 1
      if 0 <= task_num < len(tasks):
        # Mark task as done (consider using the Task class)
        tasks[task_num].done = True
        print("Task marked done.")
      else:
        print("Invalid task number.")
    else:
      print("No tasks to mark done.")
  elif choice == '4':  # Optional deletion functionality
    # Get task number to delete
    if tasks:
      task_num = int(input("Enter task number to delete (1-{}: ".format(len(tasks)))) - 1
      if 0 <= task_num < len(tasks):
        del tasks[task_num]
        print("Task deleted.")
      else:
        print("Invalid task number.")
    else:
      print("No tasks to delete.")
  elif choice == '5':
    break  # Exit the loop
  else:
    print("Invalid choice. Please try again.")

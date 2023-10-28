from tabulate import tabulate  # Import the tabulate module for formatting data as tables
import textwrap  # Import textwrap module for wrapping text to fit within specified width

def main(): # Define the main function to initiate the program
    all_tasks = []  # Initialize an empty list to store tasks
    while True:
        default_view()  # Display the default view with available options
        prompt_again(all_tasks)  # Prompt the user for input based on selected option
        print(" ")

def prompt_again(all_tasks): # Function to handle user input and perform corresponding actions
    opt = input("What do you want to do?: ")  # Prompt user for choice
    print(" ")
    while not opt.isalpha():
        print("Please enter the key next to the provided options. ")  # Ensure valid input
        print(" ")
        default_view()  # Display options again
        opt = input("What do you want to do?: ")  # Prompt user for choice again

    # Perform actions based on user's choice
    if opt.lower() == "v":
        view_task(all_tasks)
    elif opt.lower() == "a":
        add_task(all_tasks)
    elif opt.lower() == "d":
        delete_task(all_tasks)
    elif opt.lower() == "u":
        update_task(all_tasks)
    elif opt.lower() == "e":
        print("Terminating the To-do List program. See you!")  # Exit the program
        print(" ")
        exit()
    else:
        print(" ")
        print("Please enter a valid key.")

# Function to display the default view with available options
def default_view():
    print("To-do List")
    print(" ")
    # Display options as a table
    print(tabulate([["Key", "Actions"], ["V", "View all tasks"], ["A", "Add new task"],
                    ["U", "Update a task"], ["D", "Delete a task"], ["E", "Exit"]],
                   headers="firstrow", tablefmt="grid"))
    print(" ")

# Function to view all tasks
def view_task(all_tasks):
    # Enumerate tasks and display them as a table
    task_list = list(enumerate(all_tasks, start=1))
    print("All Tasks")
    print(" ")
    # Format and display tasks in a table
    if not task_list:
        all_tasks = ["You are all set!"]
        wrapped_tasks = [(idx, textwrap.fill(task, width=30)) for idx, task in enumerate(all_tasks, start=0)]
        print(tabulate(wrapped_tasks, headers=["serial no.", "Tasks"], tablefmt="grid"))
    else:
        print(tabulate(task_list, headers=["serial no.", "Tasks"], tablefmt="grid"))

# Function to add a new task
# Function to add a new task with description
def add_task(all_tasks):
    task_name = input("New task: ")  # Prompt user for task name
    task_description = input("Task description: ")  # Prompt user for task description
    new_task = f"{task_name}:- \n {task_description}"  # Create a dictionary for the new task
    print(" ")
    print("New task added to the list")
    print(" ")
    all_tasks.append(new_task)  # Add the new task to the list
    view_task(all_tasks)  # Update view after adding task

# Function to delete a task
def delete_task(all_tasks):
    if not all_tasks:
        print("No task to delete. Please add a task first.")  # Check if there are tasks to delete
        print(" ")
        return
    else:
        view_task(all_tasks)  # Display tasks to user
        delete = input("Which task do you want to delete? ")

        # Ensure valid input for task number to delete
        while not delete.isdigit() or int(delete) < 1 or int(delete) > len(all_tasks):
            print("Invalid input. Please enter a valid task number.")
            delete = input("Which task do you want to delete? ")

        all_tasks.pop(int(delete) - 1)  # Remove the selected task
        print("")
        print("Task deleted successfully.")

# Function to update a task
def update_task(all_tasks):
    if not all_tasks:
        print("No tasks to update. Please add a task first.")  # Check if there are tasks to update
        print(" ")
        return
    else:
        view_task(all_tasks)  # Display tasks to user
        update = input("Which task do you want to update? ")

        # Ensure valid input for task number to update
        while not update.isdigit() or int(update) < 1 or int(update) > len(all_tasks):
            print("Invalid input. Please enter a valid task number.")
            update = input("Which task do you want to update? ")

        updated = input("New updated task: ")  # Prompt user for updated task
        all_tasks[int(update) - 1] = updated  # Update the selected task
        print("Task updated successfully.")

# Entry point of the program, check if the script is being run directly
if __name__ == "__main__":
    main()  # Call the main function to start the program
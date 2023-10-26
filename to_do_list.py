from tabulate import tabulate
import textwrap

def main():
    all_tasks = []
    while True:
        default_view()
        prompt_again(all_tasks)
        print(" ")

def prompt_again(all_tasks):
    opt = input("What do you want to do?: ")
    print(" ")
    while not opt.isalpha():
        print("Please enter the key next to the provided options. ")
        print(" ")
        default_view()
        opt = input("What do you want to do?: ")
        
    if opt.lower() == "v":
        view_task(all_tasks)
    elif opt.lower() == "a":
        add_task(all_tasks)
    elif opt.lower() == "d":
        delete_task(all_tasks)
    elif opt.lower() == "u":
        update_task(all_tasks)
    elif opt.lower() == "e":
        print("Terminating the To-do List program. See you!")
        print(" ")
        exit()
    else:
        print(" ")
        print("Please enter a valid key.")

def default_view():
    print("To-do List")
    print(" ")
    print(tabulate([["Key","Actions"],["V","View all tasks"],["A","Add new task"],["U","Update a task"],["D","Delete a task"],["E","Exit"]],
            headers="firstrow", tablefmt="grid"))
    print(" ")

def view_task(all_tasks):
    task_list = list(enumerate(all_tasks, start=1))
    print("All Tasks")
    print(" ")
    if not task_list:
        all_tasks = ["You are all set!"]
        wrapped_tasks = [(idx, textwrap.fill(task, width=30)) for idx, task in enumerate(all_tasks, start=0)]
        print(tabulate(wrapped_tasks, headers=["serial no.", "Tasks"], tablefmt="grid"))
    else:
        print(tabulate(task_list, headers=["serial no.", "Tasks"], tablefmt="grid"))

def add_task(all_tasks):
    add = input("New task: ")
    print(" ")
    print("New task added to the list")
    print(" ")
    all_tasks.append(add)
    view_task(all_tasks)  # Update view after adding task

def delete_task(all_tasks):
    if not all_tasks:
        print("No task to delete. Please add a task first.")
        print(" ")
        return
    else:
        view_task(all_tasks)
        delete = input("Which task do you want to delete? ")

        while not delete.isdigit() or int(delete) < 1 or int(delete) > len(all_tasks):
            print("Invalid input. Please enter a valid task number.")
            delete = input("Which task do you want to delete? ")

        all_tasks.pop(int(delete) - 1)
        print("Task deleted successfully.")


def update_task(all_tasks):
    if not all_tasks:
        print("No tasks to update. Please add a task first.")
        print(" ")
        return
    else:
        view_task(all_tasks)
        update = input("Which task do you want to update? ")

        while not update.isdigit() or int(update) < 1 or int(update) > len(all_tasks):
            print("Invalid input. Please enter a valid task number.")
            update = input("Which task do you want to update? ")

        updated = input("New updated task: ")
        all_tasks[int(update) - 1] = updated
        print("Task updated successfully.")

if __name__ == "__main__":
    main()
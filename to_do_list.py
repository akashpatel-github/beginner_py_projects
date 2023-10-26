from tabulate import tabulate
import textwrap

def main():
    all_tasks = []  # Define all_tasks in the main function
    default_view()
    while True:
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
    default_view()
    all_tasks.append(add)

def delete_task(all_tasks):
    print("delete a task")

def update_task(all_tasks):
    print("update a task")

if __name__ == "__main__":
    main()
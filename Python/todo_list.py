import difflib
from emoji import emojize

todo_list = []

valid_inputs = {
    "1": "add",
    "add task": "add",

    "2": "view",
    "view task": "view",

    "3": "delete",
    "delete task": "delete",

    "4": "clear",
    "clear": "clear",

    "5": "exit",
    "exit": "exit",
}

def check_input(user_input):
    matches = difflib.get_close_matches(user_input.lower(), valid_inputs.keys(), n=1, cutoff=0.3)
    if matches:
        return valid_inputs[matches[0]]
    else:
        return None

def get_closest_task(task_name):
    matches = difflib.get_close_matches(task_name.lower(), todo_list, n=1, cutoff=0.3)
    if matches:
        return matches[0]
    else:
        print(emojize("Task not found! :magnifying_glass_tilted_left:"))
        return None

def delete_task():
    if todo_list:
        while True:
            task_to_remove = input("Enter task to delete: ").strip()
            closest_match = get_closest_task(task_to_remove)

            if task_to_remove in todo_list:
                todo_list.remove(task_to_remove)
                print(emojize("Task deleted successfully! :check_mark_button:"))
                return True

            elif closest_match:
                while True:
                    confirm = input(f"Did you mean '{closest_match}'? (Yes/No): ").strip().lower()
                    if confirm in ["yes", "y"]:
                        todo_list.remove(closest_match)
                        print(emojize("Task deleted successfully! :check_mark_button:"))
                        return True
                    elif confirm in ["no", "n"]:
                        print(f"The task named '{remove_task}' does not exist.")
                        return False
                    else:
                        print("Invalid input! Please type Yes or No.")
            else:
                return False
    else:
        print("Your to-do list is empty.")
        return False

# ----- MAIN PROGRAM -----
print(emojize("Let's create your To-Do List! :smiling_face_with_smiling_eyes:"))

is_running = True
while is_running:
    print(emojize("\n :check_mark_button: TO-DO LIST MENU"))
    print("""
    |-------------------|
    |   1. Add Task     |
    |   2. View Tasks   |
    |   3. Delete Task  |
    |   4. Clear All    |
    |   5. Exit         |
    |-------------------|""")
    user_input = input("\nChoose an option: ").strip().lower()
    action = check_input(user_input)

    if action == "add":
        task = input("Enter task to add: ").strip()
        todo_list.append(task)
        print(emojize("Your task has been added. :check_mark_button:\n"))

        while True:
            more = input("Do you want to add another task? (Yes/No): ").strip().lower()
            if more in ["yes", "y"]:
                next_task = input("Enter your next task: ").strip()
                todo_list.append(next_task)
                print(emojize("Task added. :check_mark_button:\n"))
            elif more in ["no", "n"]:
                print("Alright!")
                break
            else:
                print("Please enter Yes or No.")

    elif action == "view":
        if todo_list:
            print("\n------- Your Tasks -------")
            for i, task in enumerate(todo_list, start=1):
                print(f"     {i}. {task}")
            print("------- That's it --------\n")
        else:
            print("Your to-do list is empty.")

    elif action == "delete":
        deleted = delete_task()
        if deleted:
            while True:
                more = input("Do you want to delete another task? (Yes/No): ").strip().lower()
                if more in ["yes", "y"]:
                    delete_task()
                elif more in ["no", "n"]:
                    print("Okay!")
                    break
                else:
                    print("Please enter Yes or No.")

    elif action == "clear":
        if todo_list:
            todo_list.clear()
            print(emojize("All tasks cleared! :wastebasket:"))
        else:
            print("No tasks to clear.")

    elif action == "exit":
        print(emojize("Glad to help you! :handshake:"))
        print(emojize("Goodbye! :waving_hand:"))
        is_running = False

    else:
        print(emojize("Invalid input! Please try again. :cross_mark:"))

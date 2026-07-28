# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 7
# =============================================================================
#
# TASK: Console-Based To-Do List Application
#
# Build a simple to-do list program that runs entirely in the console and
# allows the user to manage their tasks interactively using a menu.
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Task
#      - Prompt the user to type a task description.
#      - Add it to the list and confirm it was added.
#
#   2. View All Tasks
#      - Display all tasks currently in the list, numbered from 1.
#      - If the list is empty, print a friendly message saying so.
#
#   3. Delete a Task
#      - Show the list of tasks with their numbers.
#      - Ask the user which task number they want to remove.
#      - Remove the task and confirm the deletion.
#      - If the task number is invalid, print an error message.
#
#   4. Quit
#      - End the program with a farewell message.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        TO-DO LIST MENU
#   ============================
#   1. Add task
#   2. View tasks
#   3. Delete task
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Enter task: Buy groceries
#   Task added: "Buy groceries"
#
#   Enter your choice (1-4): 1
#   Enter task: Study for exams
#   Task added: "Study for exams"
#
#   Enter your choice (1-4): 2
#   Your Tasks:
#   1. Buy groceries
#   2. Study for exams
#
#   Enter your choice (1-4): 3
#   Enter task number to delete: 1
#   Task "Buy groceries" has been removed.
#
#   Enter your choice (1-4): 4
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store tasks in a Python list.
# - Use a loop to keep the menu running until the user chooses to quit.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices gracefully (print an error, do not crash).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def print_single_table():
    """PART A: Asks for a number and prints its multiplication table from 1 to 12."""
    try:
        num = int(input("Enter a number: "))
        if num <= 0:
            print("Error: Please enter a positive integer.")
            return
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
        return

    print(f"\nMultiplication Table for {num}:")
    for i in range(1, 13):
        print(f"{num} x {i} = {num * i}")


def print_tables_up_to_n():
    """PART B (Bonus): Asks for N and prints multiplication tables from 1 up to N."""
    try:
        n = int(input("Enter a number N: "))
        if n <= 0:
            print("Error: Please enter a positive integer.")
            return
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
        return

    print()
    for current_num in range(1, n + 1):
        print(f"Multiplication Table for {current_num}:")
        for i in range(1, 13):
            print(f"{current_num} x {i} = {current_num * i}")

        # Add a separator line between tables except after the last one
        if current_num < n:
            print("-----------------------------------")


# Main execution
if __name__ == "__main__":
    print("=== PART A ===")
    print_single_table()

    print("\n=== PART B ===")
    print_tables_up_to_n()


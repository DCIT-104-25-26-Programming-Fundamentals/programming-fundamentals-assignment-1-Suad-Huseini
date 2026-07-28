# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
students = []


def display_menu():
    """Displays the main menu options."""
    print("===================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("===================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def add_student():
    """1. Add a Student: Prompts for name, ID, and scores, then saves to students list."""
    name = input("Student name: ").strip()
    student_id = input("Student ID: ").strip()

    try:
        num_scores = int(input("How many scores? "))
        if num_scores <= 0:
            print("Error: Number of scores must be greater than 0.\n")
            return
    except ValueError:
        print("Error: Please enter a valid integer for number of scores.\n")
        return

    scores = []
    for i in range(1, num_scores + 1):
        while True:
            try:
                score = float(input(f"Enter score {i}: "))
                scores.append(score)
                break
            except ValueError:
                print("Invalid score. Please enter a numerical value.")

    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }

    students.append(student)
    print(f'Student "{name}" added successfully.\n')


def display_all_students():
    """2. Display All Students: Prints a formatted table with name, ID, scores, and average."""
    if not students:
        print("No students have been added yet!\n")
        return

    print("----------------------------------------------------------------")
    print(f"{'Name':<18} {'ID':<12} {'Scores':<18} {'Average':<10}")
    print("----------------------------------------------------------------")

    for student in students:
        scores_list = student["scores"]
        scores_str = ", ".join(
            str(int(s)) if s.is_integer() else str(s) for s in scores_list
        )
        avg = sum(scores_list) / len(scores_list)

        print(f"{student['name']:<18} {student['id']:<12} {scores_str:<18} {avg:.2f}")

    print("----------------------------------------------------------------\n")


def calculate_average_for_student():
    """3. Calculate Average Score: Finds student by ID and prints their average."""
    if not students:
        print("No students have been added yet!\n")
        return

    search_id = input("Enter student ID: ").strip()

    for student in students:
        if student["id"] == search_id:
            scores_list = student["scores"]
            avg = sum(scores_list) / len(scores_list)
            print(f"{student['name']}'s average score: {avg:.2f}\n")
            return

    print(f"Error: Student with ID '{search_id}' not found.\n")


def main():
    """Main program execution loop."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            display_all_students()
        elif choice == "3":
            calculate_average_for_student()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select an option from 1 to 4.\n")


if __name__ == "__main__":
    main()

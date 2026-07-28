# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def add(a, b):
    """Performs addition."""
    return a + b


def subtract(a, b):
    """Performs subtraction."""
    return a - b


def multiply(a, b):
    """Performs multiplication."""
    return a * b


def divide(a, b):
    """Performs division, returning None if dividing by zero."""
    if b == 0:
        return None
    return round(a / b, 2)


def modulus(a, b):
    """Performs modulus, returning None if modulo by zero."""
    if b == 0:
        return None
    return a % b


def power(a, b):
    """Performs exponentiation."""
    return a ** b


def display_menu():
    """Prints the menu options."""
    print("===================================")
    print("        SIMPLE CALCULATOR")
    print("===================================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def get_number_input(prompt):
    """Helper function to repeatedly prompt until a valid number is entered."""
    while True:
        try:
            val = input(prompt).strip()
            # Convert to float if decimal point present, else int
            if "." in val:
                return float(val)
            return int(val)
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def main():
    """Main program execution loop."""
    while True:
        display_menu()
        choice = input("Select an operation (1-7): ").strip()

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice! Please select an option between 1 and 7.\n")
            continue

        # Get inputs for operations 1 to 6
        num1 = get_number_input("Enter first number : ")
        num2 = get_number_input("Enter second number: ")

        if choice == "1":
            res = add(num1, num2)
            print(f"Result: {num1} + {num2} = {res}\n")

        elif choice == "2":
            res = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {res}\n")

        elif choice == "3":
            res = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {res}\n")

        elif choice == "4":
            res = divide(num1, num2)
            if res is None:
                print("Error: Cannot divide by zero.\n")
            else:
                print(f"Result: {num1} / {num2} = {res}\n")

        elif choice == "5":
            res = modulus(num1, num2)
            if res is None:
                print("Error: Cannot perform modulus by zero.\n")
            else:
                print(f"Result: {num1} % {num2} = {res}\n")

        elif choice == "6":
            res = power(num1, num2)
            print(f"Result: {num1} ** {num2} = {res}\n")


if __name__ == "__main__":
    main()

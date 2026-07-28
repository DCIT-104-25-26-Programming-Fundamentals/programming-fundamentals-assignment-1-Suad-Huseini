# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def print_first_n_terms():
    """PART A: Asks for N and prints the first N terms of the Fibonacci sequence using a loop."""
    try:
        n = int(input("How many terms? "))
        if n <= 0:
            print("Error: Please enter a positive integer.")
            return
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
        return

    # Generate sequence using a loop
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(str(a))
        a, b = b, a + b

    print("Fibonacci sequence:", " ".join(sequence))


def check_fibonacci_number():
    """PART B: Asks for a number and determines if it belongs to the Fibonacci sequence."""
    try:
        num = int(input("Enter a number to check: "))
        if num < 0:
            print(f"{num} is NOT a Fibonacci number.")
            return
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
        return

    # Check using a loop without generating an infinite list
    a, b = 0, 1
    while a < num:
        a, b = b, a + b

    if a == num:
        print(f"{num} is a Fibonacci number.")
    else:
        print(f"{num} is NOT a Fibonacci number.")


# Main program execution
if __name__ == "__main__":
    print("--- PART A ---")
    print_first_n_terms()

    print("\n--- PART B ---")
    check_fibonacci_number()


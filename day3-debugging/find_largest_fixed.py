# find_largest_fixed.py
# This program finds the largest number in a list
# Fixed version of the buggy program

def find_largest(numbers):
    largest = numbers[0]  # Initialize to first element
    for num in numbers:
        if num > largest:
            largest = num  # Correct assignment
    return largest

# Example usage
numbers = [3, 5, 2, 8, 1]
print("The largest number is", find_largest(numbers))

# Example output:
# The largest number is 8

# calculate_average_fixed.py
# This program calculates the average of a list of numbers
# Fixed version of the buggy program

def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return average

# Example usage
numbers = [10, 20, 30, 40]
print("The average is", calculate_average(numbers))

# Example output:
# The average is 25.0

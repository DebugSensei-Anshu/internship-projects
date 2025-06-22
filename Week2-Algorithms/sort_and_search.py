# Combined Bubble Sort and Binary Search Program

# Function to perform Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

# Function to perform Binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Input from user
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Enter the target number: "))

# Sort the list using Bubble Sort
bubble_sort(numbers)
print("Sorted list:", numbers)

# Search for target using Binary Search
result = binary_search(numbers, target)
if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print(f"Target {target} not found")

# Example Run:
# Enter numbers separated by spaces: 50 10 30 20 40
# Enter the target number: 30
# Sorted list: [10, 20, 30, 40, 50]
# Target 30 found at index 2

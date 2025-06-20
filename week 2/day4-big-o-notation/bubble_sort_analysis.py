# Bubble Sort implementation and timing

import random
import time

# Generate a list of 1000 random integers between 1 and 1000
numbers = [random.randint(1, 1000) for _ in range(1000)]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Time the bubble sort
start_time = time.time()
bubble_sort(numbers.copy())  # Use a copy to preserve original list
end_time = time.time()

print("Bubble Sort Time:", end_time - start_time)

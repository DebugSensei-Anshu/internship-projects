# Python's built-in sort and timing

import random
import time

# Generate a list of 1000 random integers between 1 and 1000
numbers = [random.randint(1, 1000) for _ in range(1000)]

# Time Python's built-in sort (Timsort)
start_time = time.time()
numbers.sort()
end_time = time.time()

print("Python's Built-In Sort Time:", end_time - start_time)

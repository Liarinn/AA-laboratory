import time
import random_lists_generator as rl
import matplotlib.pyplot as plt

# A function to do counting sort of arr[] according to
# the digit represented by exp.
def countingSort(arr, exp1):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(0, n):
        index = int(arr[i] // exp1)  # Convert to int before dividing
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = int(arr[i] // exp1)  # Convert to int before dividing
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, len(arr)):
        arr[i] = output[i]

# Method to do Radix Sort
def radixSort(arr):
    max1 = max(arr)
    exp = 1
    while max1 / exp >= 1:
        countingSort(arr, exp)
        exp *= 10

# Lists generated from the separate file
lists = [rl.List_1, rl.List_2, rl.List_3, rl.List_4, rl.List_5, rl.List_6, rl.List_7, rl.List_8, rl.List_9, rl.List_10,rl.List_11,rl.List_12]

# Lists to store the time taken for each array
array_times = []

# Sort each array and store the time taken
for i, arr in enumerate(lists):
    start_time = time.time()
    radixSort(arr)
    end_time = time.time()
    time_taken = end_time - start_time
    array_times.append(time_taken)

# Plotting the graph
plt.plot(range(1, len(lists) + 1), array_times, marker='o')
plt.xlabel('Array Number')
plt.ylabel('Time Taken (seconds)')
plt.title('Time Taken to Sort Each Array using Radix Sort')
plt.xticks(range(1, len(lists) + 1))
plt.grid(True)

# Save the plot as an image file
plt.savefig('radixsort_times.png')

# Show the plot
plt.show()

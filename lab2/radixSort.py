import time
import matplotlib.pyplot as plt


def countingSort(arr, exp1):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
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


# Function to read arrays from a file
def readArraysFromFile(filename):
    arrays = []
    with open(filename, 'r') as file:
        for line in file:
            array = [int(x) for x in line.strip().split()]
            arrays.append(array)
    return arrays


# Driver code
if __name__ == '__main__':
    # Read arrays from the file
    arrays = readArraysFromFile('arrays.txt')

    # Lists to store the time taken for each array
    array_times = []

    # Sort each array and store the time taken
    for i, arr in enumerate(arrays):
        start_time = time.time()
        radixSort(arr)
        end_time = time.time()

        time_taken = end_time - start_time

        array_times.append(time_taken)

    # Plotting the graph
    plt.plot(range(1, len(arrays) + 1), array_times, marker='o')
    plt.xlabel('Array Number')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Time Taken to Sort Each Array using Radix Sort')
    plt.xticks(range(1, len(arrays) + 1))
    plt.grid(True)

    # Save the plot as an image file
    plt.savefig('radixsort_times.png')

    # Close the plot to avoid displaying it interactively
    plt.close()

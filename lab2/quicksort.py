import time
import matplotlib.pyplot as plt


# Function to find the partition position
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


# Function to perform quicksort
def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)


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
        quicksort(arr, 0, len(arr) - 1)
        end_time = time.time()

        time_taken = end_time - start_time
        array_times.append(time_taken)

    # Plotting the graph
    plt.plot(range(1, len(arrays) + 1), array_times, marker='o')
    plt.xlabel('Array Number')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Time Taken to Sort Each Array using Quicksort')
    plt.xticks(range(1, len(arrays) + 1))
    plt.grid(True)

    # Save the plot as an image file
    plt.savefig('quicksort_times.png')

    # Close the plot to avoid displaying it interactively
    plt.close()

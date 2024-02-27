import time
import matplotlib.pyplot as plt


# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, N, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < N and arr[largest] < arr[l]:
        largest = l

    if r < N and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, N, largest)


# The main function to sort an array of given size
def heapSort(arr):
    N = len(arr)

    for i in range(N // 2 - 1, -1, -1):
        heapify(arr, N, i)

    for i in range(N - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


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
        heapSort(arr)
        end_time = time.time()

        time_taken = end_time - start_time

        array_times.append(time_taken)

    # Plotting the graph
    plt.plot(range(1, len(arrays) + 1), array_times, marker='o')
    plt.xlabel('Array Number')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Time Taken to Sort Each Array using Heapsort')
    plt.xticks(range(1, len(arrays) + 1))
    plt.grid(True)

    # Save the plot as an image file
    plt.savefig('heapsort_times.png')

    # Close the plot to avoid displaying it interactively
    plt.close()

import time
import random_lists_generator as rl
import matplotlib.pyplot as plt

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)

def quicksortArraysAndPlotTimes():
    # Lists generated from the separate file
    lists = [rl.List_1, rl.List_2, rl.List_3, rl.List_4, rl.List_5, rl.List_6, rl.List_7, rl.List_8, rl.List_9, rl.List_10,rl.List_11,rl.List_12]

    # Lists to store the time taken for each array
    array_times = []

    # Sort each array and store the time taken
    for i, arr in enumerate(lists):
        start_time = time.time()
        quicksort(arr, 0, len(arr) - 1)
        end_time = time.time()
        time_taken = end_time - start_time
        array_times.append(time_taken)

    # Plotting the graph
    plt.plot(range(1, len(lists) + 1), array_times, marker='o')
    plt.xlabel('Array Number')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Time Taken to Sort Each Array using Quicksort')
    plt.xticks(range(1, len(lists) + 1))
    plt.grid(True)

    # Save the plot as an image file
    plt.savefig('quicksort_times.png')


# Call the function to execute
quicksortArraysAndPlotTimes()

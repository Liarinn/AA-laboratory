import time
import random_lists_generator as rl
import matplotlib.pyplot as plt

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def mergeSortArraysAndPlotTimes():
    # Lists generated from the separate file
    lists = [rl.List_1, rl.List_2, rl.List_3, rl.List_4, rl.List_5, rl.List_6, rl.List_7, rl.List_8, rl.List_9, rl.List_10,rl.List_11,rl.List_12]

    # Lists to store the time taken for each array
    array_times = []

    # Sort each array and store the time taken
    for i, arr in enumerate(lists):
        start_time = time.time()
        mergeSort(arr)
        end_time = time.time()
        time_taken = end_time - start_time
        array_times.append(time_taken)

    # Plotting the graph
    plt.plot(range(1, len(lists) + 1), array_times, marker='o')
    plt.xlabel('Array Number')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Time Taken to Sort Each Array using Merge Sort')
    plt.xticks(range(1, len(lists) + 1))
    plt.grid(True)

    # Save the plot as an image file
    plt.savefig('mergesort_times.png')


# Call the function to execute
mergeSortArraysAndPlotTimes()

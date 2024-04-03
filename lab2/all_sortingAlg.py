import time
import random_lists_generator as rl
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

# The main function to sort an array of given size using heapsort
def heapSort(arr):
    N = len(arr)

    for i in range(N // 2 - 1, -1, -1):
        heapify(arr, N, i)

    for i in range(N - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

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

# Function to perform mergesort
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

# Function to read arrays from a file
def readArraysFromFile(filename):
    arrays = []
    with open(filename, 'r') as file:
        for line in file:
            array = [int(x) for x in line.strip().split()]
            arrays.append(array)
    return arrays

# Lists generated from the separate file
lists = [rl.List_1, rl.List_2, rl.List_3, rl.List_4, rl.List_5, rl.List_6, rl.List_7, rl.List_8, rl.List_9, rl.List_10,rl.List_11,rl.List_12]

# Lists to store the time taken for each array for each sorting algorithm
quicksort_times = []
radixsort_times = []
heapsort_times = []
mergesort_times = []

# Sort each array and store the time taken for each sorting algorithm
for i, arr in enumerate(lists):
    start_time = time.time()
    quicksort(arr.copy(), 0, len(arr) - 1)
    end_time = time.time()
    quicksort_times.append(end_time - start_time)

    start_time = time.time()
    radixSort(arr.copy())
    end_time = time.time()
    radixsort_times.append(end_time - start_time)

    start_time = time.time()
    heapSort(arr.copy())
    end_time = time.time()
    heapsort_times.append(end_time - start_time)

    start_time = time.time()
    mergeSort(arr.copy())
    end_time = time.time()
    mergesort_times.append(end_time - start_time)

# Plotting the graph for all sorting algorithms
plt.plot(range(1, len(lists) + 1), quicksort_times, marker='o', label='Quicksort')
plt.plot(range(1, len(lists) + 1), radixsort_times, marker='o', label='Radix Sort')
plt.plot(range(1, len(lists) + 1), heapsort_times, marker='o', label='Heapsort')
plt.plot(range(1, len(lists) + 1), mergesort_times, marker='o', label='Mergesort')

plt.xlabel('Array Number')
plt.ylabel('Time Taken (seconds)')
plt.title('Time Taken to Sort Each Array using Different Sorting Algorithms')
plt.xticks(range(1, len(lists) + 1))
plt.grid(True)
plt.legend()

# Save the plot as an image file
plt.savefig('all_sorting_algorithms.png')

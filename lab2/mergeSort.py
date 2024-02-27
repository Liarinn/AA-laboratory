import time
import matplotlib.pyplot as plt


def mergeSort(arr):
	if len(arr) > 1:

		# Finding the mid of the array
		mid = len(arr)//2

		# Dividing the array elements
		L = arr[:mid]

		# Into 2 halves
		R = arr[mid:]

		# Sorting the first half
		mergeSort(L)

		# Sorting the second half
		mergeSort(R)

		i = j = k = 0

		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# Function to read arrays from a file
def readArraysFromFile(filename):
    arrays = []
    with open(filename, 'r') as file:
        for line in file:
            array = [int(x) for x in line.strip().split()]
            arrays.append(array)
    return arrays


if __name__ == '__main__':
	# Read arrays from the file
	arrays = readArraysFromFile('arrays.txt')

	# Lists to store the time taken for each array
	array_times = []

	# Sort each array and store the time taken
	for i, arr in enumerate(arrays):
		start_time = time.time()
		mergeSort(arr)
		end_time = time.time()

		time_taken = end_time - start_time


		array_times.append(time_taken)

	# Plotting the graph
	plt.plot(range(1, len(arrays) + 1), array_times, marker='o')
	plt.xlabel('Array Number')
	plt.ylabel('Time Taken (seconds)')
	plt.title('Time Taken to Sort Each Array')
	plt.xticks(range(1, len(arrays) + 1))
	plt.grid(True)

	# Save the plot as an image file
	plt.savefig('sorting_times_mergesort.png')

	# Close the plot to avoid displaying it interactively
	plt.close()





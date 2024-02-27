import time
import matplotlib.pyplot as plt
from tabulate import tabulate
def Fibonacci(n):
    l1 = [0,1]

    for i in range(2, n+1):
        l1.append(l1[i-1] + l1[i-2])
    return l1[n]
#[2, 4, 6, 8, 12, 14, 17, 19, 22, 25, 27, 29, 33, 36, 38, 41, 44]
nums = [450, 500, 590, 650, 734, 811, 991, 1197, 1300, 1487, 1603, 1788, 1945, 2355, 2789, 3454, 4382, 5000, 5777, 6540, 8245, 9984, 11113, 14545, 16234]
elapsed_times = []

for x in nums:
    term_start_time = time.time()
    Fibonacci(x)
    term_end_time = time.time()
    elapsed_time = term_end_time - term_start_time
    elapsed_times.append(elapsed_time)

print("Elapsed times for each term:", elapsed_times)
results_table = tabulate(zip(nums, elapsed_times), headers=['N-th Fibonacci Term', 'Time (s)'], tablefmt='grid')
print(results_table)

# Plotting the graph
plt.plot(nums, elapsed_times, marker='o')
plt.title('Dynamic Programming Method')
plt.xlabel('n-th Fibonacci Term')
plt.ylabel('Time (s)')
plt.grid(True)

# Save the plot as an image file
plt.savefig('fibonacci_time_plot22.png')

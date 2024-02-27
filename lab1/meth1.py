import time
import matplotlib.pyplot as plt

def Fibonacci(n):
    if  n <= 1:
        return n
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

nums = [2, 4, 6, 8, 12, 14, 17, 19, 22, 25, 27, 29, 33, 36, 38, 41, 44]
elapsed_times = []

for x in nums:
    term_start_time = time.time()
    Fibonacci(x)
    term_end_time = time.time()
    elapsed_time = term_end_time - term_start_time
    elapsed_times.append(elapsed_time)

print("Elapsed times for each term:", elapsed_times)

# Plotting the graph
plt.plot(nums, elapsed_times, marker='o')
plt.title('Recursive Method')
plt.xlabel('n-th Fibonacci Term')
plt.ylabel('Time (s)')
plt.grid(True)

# Save the plot as an image file
plt.savefig('fibonacci_time_plot1.png')

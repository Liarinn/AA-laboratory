import time
import matplotlib.pyplot as plt

def Fibonacci(n):
    if n < 2:
        return n
    fs = [0, 1]
    for i in range(1, n):
        fs.append(fs[i] + fs[i - 1])
    return fs[n]


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

# Plotting the graph
plt.plot(nums, elapsed_times, marker='o')
plt.title('Iteration Method')
plt.xlabel('n-th Fibonacci Term')
plt.ylabel('Time (s)')
plt.grid(True)

# Save the plot as an image file
plt.savefig('fibonacci_time_plot55.png')

import time
import matplotlib.pyplot as plt


PHI = 16180339
f = [0, 1, 1, 2, 3, 5]

def fib(n):
    if n < 6:
        return f[n]
    t = 5
    fn = 5

    while t < n:
        fn = (fn * PHI) // 10000000
        t += 1

    return fn

#[2, 4, 6, 8, 12, 14, 17, 19, 22, 25, 27, 29, 33, 36, 38, 41, 44]
nums = [450, 500, 590, 650, 734, 811, 991, 1197, 1300, 1487, 1603, 1788, 1945, 2355, 2789, 3454, 4382, 5000, 5777, 6540, 8245, 9984, 11113, 14545, 16234]
elapsed_times = []

for x in nums:
    term_start_time = time.time()
    fib(x)
    term_end_time = time.time()
    elapsed_time = term_end_time - term_start_time
    elapsed_times.append(elapsed_time)

print("Elapsed times for each term:", elapsed_times)

# Plotting the graph
plt.plot(nums, elapsed_times, marker='o')
plt.title('Golden Ratio Formula Method')
plt.xlabel('n-th Fibonacci Term')
plt.ylabel('Time (s)')
plt.grid(True)

# Save the plot as an image file
plt.savefig('fibonacci_time_plot66.png')

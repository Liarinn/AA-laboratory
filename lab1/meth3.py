import time
import matplotlib.pyplot as plt

def power(F,n):
    M = [[1,1],
         [1,0]]
    for i in range(2, n+1):
        multiply(F,M)
def Fibonacci(n):
    F = [[1,1],
         [1,0]]
    if (n==0):
        return 0
    power(F, n-1)

    return F[0][0]

def multiply(F, M):
    x = (F[0][0] * M[0][0] + F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] + F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] + F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] + F[1][1] * M[1][1])

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w

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
plt.title('Matrix Power Method')
plt.xlabel('n-th Fibonacci Term')
plt.ylabel('Time (s)')
plt.grid(True)

# Save the plot as an image file
plt.savefig('fibonacci_time_plot33.png')

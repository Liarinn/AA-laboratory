import time
from decimal import *
from tabulate import tabulate

from tabulate import tabulate
def Fibonacci2(n):
    l1 = [0,1]

    for i in range(2, n+1):
        l1.append(l1[i-1] + l1[i-2])
    return l1[n]


def power(F,n):
    M = [[1,1],
         [1,0]]
    for i in range(2, n+1):
        multiply(F,M)
def Fibonacci3(n):
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

def Fibonacci4(n):
    ctx = Context(prec=60, rounding=ROUND_HALF_EVEN)
    sq5 = Decimal(5 ** 0.5)
    phi = Decimal(sq5 + 1) / 2
    fib = (ctx.power(phi, Decimal(n)) - ctx.power(-phi, -n)) / sq5
    return int(fib)

def Fibonacci5(n):
    if n < 2:
        return n
    fs = [0, 1]
    for i in range(1, n):
        fs.append(fs[i] + fs[i - 1])
    return fs[n]

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

nums = [450, 500, 590, 650, 734, 811, 991, 1197, 1300, 1487, 1603, 1788, 1945, 2355, 2789, 3454, 4382, 5000, 5777, 6540, 8245, 9984, 11113, 14545, 16234]


elapsed_times2 = []
for x in nums:
    term_start_time2 = time.time()
    Fibonacci2(x)
    term_end_time2 = time.time()
    elapsed_time2 = term_end_time2 - term_start_time2
    elapsed_times2.append(elapsed_time2)

elapsed_times3 = []
for x in nums:
    term_start_time = time.time()
    Fibonacci3(x)
    term_end_time = time.time()
    elapsed_time = term_end_time - term_start_time
    elapsed_times3.append(elapsed_time)

elapsed_times4 = []
for x in nums:
    term_start_time = time.time()
    Fibonacci4(x)
    term_end_time = time.time()
    elapsed_time = term_end_time - term_start_time
    elapsed_times4.append(elapsed_time)

elapsed_times5 = []
for x in nums:
    term_start_time = time.time()
    Fibonacci5(x)
    term_end_time = time.time()
    elapsed_time = term_end_time - term_start_time
    elapsed_times5.append(elapsed_time)

elapsed_times6 = []
for x in nums:
    term_start_time = time.time()
    fib(x)
    term_end_time = time.time()
    elapsed_time = term_end_time - term_start_time
    elapsed_times6.append(elapsed_time)


# Create the table
table_data = []
for i, n in enumerate(nums):
    table_data.append([n,  elapsed_times2[i], elapsed_times3[i], elapsed_times4[i], elapsed_times5[i], elapsed_times6[i]])

headers = ["Nth Term",  "Method 2", "Method 3", "Method 4", "Method 5", "Method 6"]
print(tabulate(table_data, headers=headers))
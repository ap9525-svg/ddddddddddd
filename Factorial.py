import time

# -------- Factorial without Recursion --------
def nrec(n):
    r = 1
    for i in range(1, n + 1):
        r = r * i
    return r

# -------- Factorial using Recursion --------
def rec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * rec(n - 1)

# -------- Main Program --------
n = int(input("Enter a number: "))

# Recursive method timing
start = time.time()
res1 = rec(n)
end = time.time()
time1 = end - start

print("\nFactorial using recursion:", res1)
print("Execution time (recursion): {:.10f} seconds".format(time1))

# Non-recursive method timing
start = time.time()
res2 = nrec(n)
end = time.time()
time2 = end - start

print("\nFactorial without recursion:", res2)
print("Execution time (without recursion): {:.10f} seconds".format(time2))

import time

def wrec(a):
    sum = 0
    for i in a:
        sum += i
    return sum

def rec(a, n):
    if n == 0:
        return 0
    else:
        return a[n-1] + rec(a, n-1)

print("Enter the numbers separated by spaces")

a = list(map(int, input().split()))
print("Array elements are", a)

start = time.time()
t1 = wrec(a)
end = time.time()
print("Sum without recursion is", t1)
print("Execution time without recursion", end-start)

start1 = time.time()
t2 = rec(a, len(a))
end1 = time.time()
print("Sum with recursion is", t2)
print("Execution time with recursion is", end1-start1)
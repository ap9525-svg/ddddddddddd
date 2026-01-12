import time

# -------- Input Array --------
n = int(input("Enter the size of the array: "))
arr = []

for i in range(n):
    user = int(input("Enter the number: "))
    arr.append(user)

# -------- Linear Search Function --------
def search(arr):
    k= int(input("Enter the element to find: "))
    for i in range(len(arr)):
        if arr[i] == k:
            return i + 1  # position starting from 1
    return -1

# -------- Timing the Search --------
start = time.time()
res = search(arr)
end = time.time()
total_time = end - start

# -------- Print Result --------
if res == -1:
    print("Key not found")
else:
    print("Key is found at position", res)

print("Execution time for linear search: {:.10f} seconds".format(total_time))

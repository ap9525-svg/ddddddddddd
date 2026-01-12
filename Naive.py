import time

def naive(p, t):
    m, n = len(p), len(t)
    pos = []

    for i in range(n - m + 1):
        j = 0
        while j < m and t[i + j] == p[j]:
            j += 1
        if j == m:
            pos.append(i + 1)   # position

    return pos


# ---- Main ----
t = input("Enter text: ")
p = input("Enter pattern: ")

st = time.time()
r = naive(p, t)
et = time.time()

if r:
    print("Pattern found at:", r)
else:
    print("Pattern not found")

print("Execution time:", et - st)


























"""



import time

def naive_search(pattern, text):
    pattern_length = len(pattern)
    text_length = len(text)
    positions = []

    for i in range(text_length - pattern_length + 1):
        j = 0
        while j < pattern_length and text[i + j] == pattern[j]:
            j += 1
        if j == pattern_length:
            positions.append(i+1)  # 0-based index

    return positions


# -------- Main Program --------
text = input("Enter a text: ")
pattern = input("Enter the pattern to search: ")

start = time.time()
result = naive_search(pattern, text)
end = time.time()

if result:
    print("Pattern found at positions:", result)
else:
    print("Pattern not found")

print("Execution time: {:.10f} seconds".format(end - start))

"""
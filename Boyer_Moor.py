import time

num = 256

def Char(pat):
    bad = [-1] * num
    for i in range(len(pat)):
        bad[ord(pat[i])] = i
    return bad

def search(txt, pat):
    m = len(pat)
    n= len(txt)
    bad = Char(pat)
    s = 0
    found = False   # flag to check pattern found

    while s <= n - m:
        j = m - 1
        while j >= 0 and pat[j] == txt[s + j]:
            j -= 1

        if j < 0:
            print("Pattern found at index", s)
            found = True
            s += 1
        else:
            s += max(1, j - bad[ord(txt[s + j])])

    if not found:
        print("Pattern not found")

txt = "ABAAABCD"
pat = "ABCw"

start = time.time()
search(txt, pat)
end = time.time()

print("Execution time:", end - start)
























"""
import time

NO_OF_CHARS = 256

def bad_char_table(pattern):
    table = [-1] * NO_OF_CHARS

    for i in range(len(pattern)):
        table[ord(pattern[i])] = i

    return table

# Step 2: Search function
def boyer_moore(text, pattern):
    text_length = len(text)
    # text length
    pattern_length = len(pattern)
    # pattern length


    bad_char = bad_char_table(pattern)
    shift = 0   # how much pattern is shifted
    found = False

    while shift <= text_length - pattern_length:
        j = pattern_length - 1   # start comparing from last character

        # move from right to left
        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1

        # pattern matched
        if j < 0:
            print("Pattern found at index", shift)
            #shift +=(pattern_length - bad_char[ord(text[shift+pattern_length])] if shift+pattern_length < text_length else 1)
            shift+=1
            found = True
        # mismatch
        else:
            shift += max(1, j - bad_char[ord(text[shift + j])])

    if not found:
        print("pattern not found")



txt = "ABCDEFGHIJKLMNOPQUSTUVWXYZ"
pat = "XYZa"

boyer_moore(txt, pat)

start = time.time()
end = time.time()

print("Time taken:", end - start)

"""
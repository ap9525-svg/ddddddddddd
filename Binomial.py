def binomial(n,r):
    if r==0:
        return 1
    if n==r:
        return 1
    else:
        return binomial(n-1,r) + binomial(n-1,r-1)


n = int(input("Enter the value for n"))
r = int(input("Enter the value for r"))

if r>n:
    print("Enter the value on n greater than r or e")
else:
    result = binomial(n,r)
    print(result)
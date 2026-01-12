import time
def wrec(a,n):
    sum=0
    for i in range(n):
        sum=sum+a[i]
    return sum
    
def rec(a,n):
    if n==0:
        return 0
    else:
        return a[n-1] + rec(a,n-1) 
    
a=[]
n=int(input("enter number of element:"))
for i in range(n):
    x=int(input("enter the element"))
    a.append(x)
start=time.time()
result1=wrec(a,n)
end=time.time()
time1=end-start
print("\n sum element without Recurcive:",result1)
print("Execution time taken (Without recurcive): {:.10f}".format(time1))

start=time.time()
result2=rec(a,n)
end=time.time()
time2=end-start
print("sum With recurcive ",result2)
print("Execution time taken (With Recurcive): {:.10f}".format(time2))
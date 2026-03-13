import time

def war(graph,n):
    tc = [row[:] for row in graph]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                tc[i][j] = tc[i][j] or (tc[i][k] and tc[k][j])

    return tc

n = int(input("Enter the number of vertices: "))
print("Enter adjacency matrix")
graph = []

for i in range(n):
    row = list(map(int,input().split()))
    graph.append(row)

start= time.time()
tc = war(graph,n)
end = time.time()
time = end-start

print("\n transitive closure matirix: ")
for row in tc:
    print(*row)
print("execution time of warshall algorihtm : {:.10f} seconds".format(time))
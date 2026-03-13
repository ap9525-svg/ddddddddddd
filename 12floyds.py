INF = 999

def floyd(dist, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


n = int(input("Enter number of vertices: "))
print("Enter adjacency matrix:")
print("Enter 0 for no edge (except diagonal)")

dist = []

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if i != j and row[j] == 0:
            row[j] = INF
    dist.append(row)

result = floyd(dist, n)

print("\nAll Pairs Shortest Path Matrix:")
for row in result:
    print(*row)
INFINITY = 999

def dijkstra(n, source, cost):
    dist = [INFINITY] * (n + 1)
    visited = [False] * (n + 1)
    dist[source] = 0

    for _ in range(n):
        u = min((w for w in range(1, n + 1) if not visited[w]), key=lambda w: dist[w], default=-1)
        if u == -1 or dist[u] == INFINITY:
            break
        visited[u] = True
        for w in range(1, n + 1):
            if not visited[w] and dist[u] + cost[u][w] < dist[w]:
                dist[w] = dist[u] + cost[u][w]

    return dist


n = int(input("Enter the number of nodes: "))
cost = [[INFINITY] * (n + 1) for _ in range(n + 1)]

print("Enter the cost matrix:")
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        cost[i][j] = INFINITY if row[j-1] == 0 else row[j-1]

source = int(input("Enter the source node: "))
dist = dijkstra(n, source, cost)

print(f"\nShortest paths from source node {source}:")
for i in range(1, n + 1):
    if i != source:
        print(f"  {source} -> {i} : Cost = {dist[i] if dist[i] != INFINITY else 'unreachable'}")
INF = 999

n = int(input("Enter the number of nodes: "))

cost = [[0]*(n+1) for _ in range(n+1)]

print("Enter the adjacency matrix:")
for i in range(1, n+1):
    row = list(map(int, input().split()))
    for j in range(1, n+1):
        cost[i][j] = row[j-1]
        if cost[i][j] == 0:
            cost[i][j] = INF

visited = [0]*(n+1)
visited[1] = 1

ne = 1
minicost = 0

while ne < n :
    minimum = INF
    for i in range(1, n+1):
        if visited[i]:
            for j in range(1, n+1):
                if cost[i][j] < minimum:
                    minimum = cost[i][j]
                    a = i
                    b = j
                    if not visited[b]:
                        print("edge",ne,":",a,"-",b,"cost =",minimum)
                        visited[b]=1
                        minicost += minimum
                        ne +=1
                        cost[a][b]=cost[b][a]=INF
print("minimum cost:", minicost)
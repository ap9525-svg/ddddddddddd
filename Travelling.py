def get():
    n = int(input("Enter No. of cities: "))
    a = [list(map(int, input(f"Row {i+1}: ").split())) for i in range(n)]
    return n, a

# def display(a, n):
#     print("\nCost Matrix:")
#     print("    " + "  ".join(f"C{j+1}" for j in range(n)))
#     for i, row in enumerate(a):
#         print(f"C{i+1}  " + "  ".join(f"{v:2}" for v in row))

def least(a, visited, c, n):
    options = [(a[c][i], i) for i in range(n) if a[c][i] != 0 and not visited[i]]
    return min(options, default=(999, 999))

def mincost(a, n):
    visited = [False] * n
    city, total, path = 0, 0, [0]
    visited[0] = True

    for _ in range(n - 1):
        cost, nc = least(a, visited, city, n)
        if nc == 999: break
        total += cost
        visited[nc] = True
        path.append(nc)
        city = nc

    total += a[city][0]
    path.append(0)
    return path, total

if __name__ == "__main__":
    n, a = get()
    #display(a, n)
    path, cost = mincost(a, n)
    print("\nPath:", " -> ".join(str(p + 1) for p in path))
    print("Minimum cost:", cost)

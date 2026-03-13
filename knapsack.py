# Function for Knapsack using Memoization
def knapsack(W, wt, val, n, memo):

    # Base condition
    if n == 0 or W == 0:
        return 0

    # If value already calculated
    if memo[n][W] != -1:
        return memo[n][W]

    # If weight of the nth item is more than capacity
    if wt[n-1] > W:
        memo[n][W] = knapsack(W, wt, val, n-1, memo)
        return memo[n][W]

    else:
        include = val[n-1] + knapsack(W - wt[n-1], wt, val, n-1, memo)
        exclude = knapsack(W, wt, val, n-1, memo)

        memo[n][W] = max(include, exclude)
        return memo[n][W]


# Driver Code
W = 7
wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]
n = len(val)

# Create memo table
memo = [[-1 for i in range(W + 1)] for j in range(n + 1)]

result = knapsack(W, wt, val, n, memo)

print("Maximum value in Knapsack =", result)
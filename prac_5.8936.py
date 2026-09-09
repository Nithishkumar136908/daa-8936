# 0/1 Knapsack using Dynamic Programming

n = int(input("Enter number of items: "))

weight = list(map(int, input("Enter weights: ").split()))
value = list(map(int, input("Enter values: ").split()))

W = int(input("Enter capacity: "))

# Create DP table
dp = [[0 for w in range(W + 1)] for i in range(n + 1)]

# Fill DP table
for i in range(1, n + 1):
    for w in range(1, W + 1):

        if weight[i - 1] <= w:
            dp[i][w] = max(
                value[i - 1] + dp[i - 1][w - weight[i - 1]],
                dp[i - 1][w]
            )
        else:
            dp[i][w] = dp[i - 1][w]

# Maximum profit
print("\nMaximum Profit =", dp[n][W])

# Find selected items
print("Selected Items:", end=" ")

w = W

for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        print("Item", i, end=" ")
        w = w - weight[i - 1]

# Find selected weights
print("\nSelected Weights:", end=" ")

w = W

for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        print(weight[i - 1], end=" ")
        w = w - weight[i - 1]

print()
A = input()
B = input()

# Please write your code here.
dp = [[0 for _ in range(len(A) + 1)] for _ in range(len(B) + 1)]

for i in range(1, len(B) + 1):
    for j in range(1, len(A) + 1):
        if A[j-1] != B[i-1]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        else:
            dp[i][j] = dp[i-1][j-1] + 1

print(dp[len(B)][len(A)])
# for i in range(len(B) + 1):
#     print(*dp[i])
        
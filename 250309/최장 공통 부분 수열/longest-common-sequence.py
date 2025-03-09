A = input()
B = input()

# Please write your code here.
dp = [[0 for _ in range(len(A))] for _ in range(len(B))]

for i in range(len(B)):
    dp[i][0] = 1

for j in range(len(A)):
    dp[0][j] = 1

for i in range(1, len(B)):
    for j in range(1, len(A)):
        if A[j-1] != B[i-1]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            continue
        dp[i][j] = dp[i-1][j-1] + 1

print(dp[len(B)-1][len(A)-1])
# for i in range(len(B)):
#     print(*dp[i])
        
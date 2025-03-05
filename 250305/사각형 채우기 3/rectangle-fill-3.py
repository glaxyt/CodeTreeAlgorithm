n = int(input())

# Please write your code here.
memo = [0] * (n+3)
accumulate_total = [0] * (n+3)

memo[0] = 1
memo[1] = 2
memo[2] = 7
memo[3] = 22

def dp(n):
    if n <= 3:
        return memo[n]
    else:
        for i in range(4, n+1):
            memo[i] = ((2 * memo[i-1]) + (3 * memo[i-2]) + (2 * memo[i-3])) % 1000000007
    return memo[n]

print(dp(n))
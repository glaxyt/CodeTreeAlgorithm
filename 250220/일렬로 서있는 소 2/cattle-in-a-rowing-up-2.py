N = int(input())
A = list(map(int, input().split()))

# Write your code here!
ans = 0
for i in range(N):
    for j in range(i, N):
        for k in range(j, N):
            if A[i] < A[j] and A[j] < A[k]:
                ans += 1

print(ans)
n = int(input())
A = list(map(int, input().split()))

# Write your code here!
ans = []

for i in range(n):
    total = 0
    for j in range(n):
        if i == j:
            continue
        total += abs(i-j) * A[j]
    ans.append(total)

print(min(ans))
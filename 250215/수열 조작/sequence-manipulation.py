from collections import deque

n = int(input())

# Write your code here!
dq = deque([i for i in range(1, n+1)])

while len(dq) > 1:
    dq.popleft()
    num = dq.popleft()
    dq.append(num)

print(dq.popleft())


from collections import deque

n = int(input())
num = list(map(int, input().split()))
visited = [False] * n
# Please write your code here.
queue = deque([0])
visited[0] = 1

while queue:
    cx = queue.pop()
    
    if cx == n-1:
        print(visited[cx] - 1)
        break

    jump = num[cx]

    for i in range(1, jump + 1):
        nx = cx + i
        if 0 <= nx < n and not visited[nx]:
            visited[nx] = visited[cx] + 1
            queue.appendleft(nx)
else:
    print(-1)
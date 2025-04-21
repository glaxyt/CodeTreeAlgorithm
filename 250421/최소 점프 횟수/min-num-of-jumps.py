from collections import deque

n = int(input())
num = list(map(int, input().split()))
visited = [False] * n
queue = deque()
queue.append((0, 0))  # (현재 index, 점프 횟수)

while queue:
    idx, cnt = queue.popleft()
    
    if idx == n - 1:
        print(cnt)
        break
    
    for i in range(1, num[idx] + 1):
        next_idx = idx + i
        if next_idx < n and not visited[next_idx]:
            visited[next_idx] = True
            queue.append((next_idx, cnt + 1))
else:
    print(-1)

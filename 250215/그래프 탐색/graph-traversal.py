

def dfs(node):
    global ans
    for nextNode in graph[node]:
        if not visited[nextNode]:
            ans += 1
            visited[nextNode] = True
            dfs(nextNode)
    return ans

n, m = map(int, input().split())

# Write your code here!
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[1] = True
ans = 0
print(dfs(1))


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dxys = ((1,0), (0,1))
# Write your code here!
def dfs(cx, cy):
    if (cx, cy) == (n-1, m-1):
        return True
    for dx, dy in dxys:
        nx = cx + dx
        ny = cy + dy
        if 0 <= ny < n and 0 <= nx < m:
            if grid[ny][nx] == 1 and visited[ny][nx] == False:
                visited[ny][nx] = True;
                if dfs(nx, ny):
                    return True;

    return False;

visited[0][0] = True
ans = 0

if dfs(0, 0):
    print(1)
else:
    print(0)

    
        

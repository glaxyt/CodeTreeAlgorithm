n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
dirs = ((-1, 0), (-1, 1), (0, 1), (1,1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solution():
    answer = []

    def backtracking(cx, cy, cnt):
        # n = 3이라면 *1, *2, *3으로 해결
        offset = move_dir[cx][cy]
        dx, dy = dirs[offset-1]
        for i in range(1, n + 1):
            nx = cx + (dx * i)
            ny = cy + (dy * i)
            if 0 <= nx < n and 0 <= ny < n:
                if num[nx][ny] > num[cx][cy]:
                    backtracking(nx, ny, cnt + 1)
            else:
                answer.append(cnt)

        
    backtracking(r-1, c-1, 0)
    return max(answer)

print(solution())
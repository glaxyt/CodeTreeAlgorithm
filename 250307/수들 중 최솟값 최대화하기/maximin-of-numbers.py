import heapq

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
col_visited = [False for _ in range(n)]
answer = []
sum_ans = []
# Please write your code here.
def permutation_get_min_arg(cur_row):
    if cur_row == n:
        heapq.heappush(sum_ans, -1 * min(answer))
        return

    for cur_col in range(n):
        if col_visited[cur_col]:
            continue

        col_visited[cur_col] = True
        answer.append(grid[cur_row][cur_col])

        permutation_get_min_arg(cur_row + 1)

        answer.pop()
        col_visited[cur_col] = False

permutation_get_min_arg(0)
print(-1 * heapq.heappop(sum_ans))
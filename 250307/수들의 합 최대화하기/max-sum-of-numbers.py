def back_tracking(cur_num):
    if cur_num == n:
        sum_ans.append(sum(answer))
        return

    for i in range(n):
        if col[i]:
            continue

        col[i] = True

        answer.append(grid[cur_num][i])

        back_tracking(cur_num + 1)

        answer.pop()

        col[i] = False


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
row = [False for _ in range(n)]
col = [False for _ in range(n)]
answer = []
sum_ans = []

back_tracking(0)
print(max(sum_ans))

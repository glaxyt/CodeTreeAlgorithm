def back_tracking(cur_num):
    if cur_num == n:
        sum_ans.append(sum(answer))
        return

    for i in range(n):
        for j in range(n):
            if row[i] or col[j]:
                continue

            row[i] = True
            col[j] = True

            answer.append(grid[i][j])

            back_tracking(cur_num + 1)

            answer.pop()

            row[i] = False
            col[j] = False


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
row = [False for _ in range(n)]
col = [False for _ in range(n)]
answer = []
sum_ans = []

back_tracking(0)
print(max(sum_ans))

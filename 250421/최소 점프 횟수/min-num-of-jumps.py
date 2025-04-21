n = int(input())
num = list(map(int, input().split()))
answer = []
visited = [100] * n
# Please write your code here.
def backtracking(currentIdx, cnt):
    
    if currentIdx == n-1:
        answer.append(cnt)
        return

    if cnt > visited[currentIdx]:
        return

    jump = num[currentIdx]
    for nextIdx in range(currentIdx, currentIdx + jump + 1):
        if nextIdx >= n:
            continue 

        backtracking(nextIdx, cnt + 1)

visited[0] = 0
backtracking(0, 0)
if answer:
    print(min(answer))
else:
    print(-1)
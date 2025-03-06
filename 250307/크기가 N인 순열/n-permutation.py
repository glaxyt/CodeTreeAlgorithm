def back_tracking():
    if len(answer) == n:
        print(*answer)
        return 

    for idx in range(1, n+1):
        if visited[idx]:
            continue

        visited[idx] = True
        answer.append(nums[idx])

        back_tracking()

        visited[idx] = False
        answer.pop()
    

n = int(input())
nums = [i for i in range(n+1)]
visited = [False for _ in range(n+1)]
# Please write your code here.

answer = []

back_tracking()
n = int(input())
li = list(map(int, input().split()))
ans = []
for i in range(1, n+1):
    if not i % 2:
        continue
    cur_li = sorted(li[:i])
    print(cur_li[(i-1)//2], end = " ")

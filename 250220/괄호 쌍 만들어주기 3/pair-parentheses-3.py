li = list(input())
# for i in range(n)
ans = 0

for i in range(len(li)):
    first_word = li[i]
    if first_word == ")":
        continue
    for j in range(i, len(li)):
        if first_word != li[j]:
            ans += 1

print(ans)

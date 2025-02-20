_ = input()
li = list(map(int, input().split()))

print(*sorted(li))
print(*sorted(li, reverse = True))

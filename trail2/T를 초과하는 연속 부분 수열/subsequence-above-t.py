n, t = map(int, input().split())
arr = list(map(int, input().split()))

ans = cnt = 0
for x in arr:
    if x > t:
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 0

print(ans)
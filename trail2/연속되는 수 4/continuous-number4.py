n = int(input())
arr = [int(input()) for _ in range(n)]

ans, cnt = 1, 1
for i in range(n-1):
    if arr[i] < arr[i+1]:
        cnt += 1
    else:
        cnt = 1
    
    ans = max(ans, cnt)

print(ans)

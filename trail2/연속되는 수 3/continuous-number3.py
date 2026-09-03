n = int(input())
arr = [int(input()) for _ in range(n)]

count = 1
max_count = 1

for i in range(n-1):
    if arr[i] > 0:
        if arr[i+1] > 0:
            count += 1
        else:
            count = 1
        if count >= max_count:
            max_count = count
    else:
        if arr[i+1] < 0:
            count += 1
        else:
            count = 1
        if count>= max_count:
            max_count = count

print(max_count)
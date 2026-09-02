n = int(input())
arr = [int(input()) for _ in range(n)]

count = 1
max_count = 1

for i in range(n-1):
    if arr[i] == arr[i+1]:
        count += 1
        if count >= max_count:
            max_count = count
    else:
        if count >= max_count:
            max_count = count
        count = 1

print(max_count)
n = int(input())

arr = [0] * 2001
cur = 1000

for _ in range(n):
    x, dir = input().split()
    x = int(x)

    if dir == 'R':
        for i in range(cur, cur + x):
            arr[i] += 1
        cur += x

    else:
        for i in range(cur - x, cur):
            arr[i] += 1
        cur -= x

print(sum(1 for x in arr if x >= 2))
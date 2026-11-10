def find_min(n,m):
    min = 1
    num = max(n, m)
    while 1:
        if (num % n == 0) & (num % m == 0):
            min = num
            break
        else:
            num += 1
    return num

n, m = map(int, input().split())
print(find_min(n,m))

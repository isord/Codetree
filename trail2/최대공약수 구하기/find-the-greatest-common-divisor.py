def max(n,m):
    num = 1
    ber = 1
    while num <= n:
        if (n % num == 0) & (m % num == 0):
            ber = num
            num += 1
        else:
            num += 1
    return(ber)

n,m = map(int,input().split())
print(max(n,m))
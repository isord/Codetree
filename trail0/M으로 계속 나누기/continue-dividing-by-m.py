N, M = map(int, input().split())

# Please write your code here.
while N >= M:
    print(int(N))
    N /= M
print(int(N))
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

def dist(a, b):
    return abs(x[a] - x[b]) + abs(y[a] - y[b])

total = sum(dist(i, i + 1) for i in range(n - 1))

ans = min(
    total - dist(i - 1, i) - dist(i, i + 1) + dist(i - 1, i + 1)
    for i in range(1, n - 1)
)

print(ans)
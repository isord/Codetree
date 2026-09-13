n = int(input())
grid = [[0] * n for _ in range(n)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

x = y = n // 2
grid[x][y] = 1
num = 1
d = 0
step = 1

while num < n * n:
    for _ in range(2):
        for _ in range(step):
            if num >= n * n:
                break
            x += dx[d]
            y += dy[d]
            num += 1
            grid[x][y] = num
        d = (d + 1) % 4
    step += 1

for row in grid:
    print(*row)
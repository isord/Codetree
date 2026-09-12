n, m = map(int, input().split())

grid = [[''] * m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y, d = 0, 0, 0

for i in range(n * m):
    grid[x][y] = chr(ord('A') + i % 26)

    nx, ny = x + dx[d], y + dy[d]
    if not (0 <= nx < n and 0 <= ny < m) or grid[nx][ny]:
        d = (d + 1) % 4
        nx, ny = x + dx[d], y + dy[d]

    x, y = nx, ny

for row in grid:
    print(' '.join(row))
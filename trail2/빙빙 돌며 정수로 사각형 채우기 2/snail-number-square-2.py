n, m = map(int, input().split())

arr = [[0] * m for _ in range(n)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

r, c, d = 0, 0, 0

for num in range(1, n * m + 1):
    arr[r][c] = num

    nr, nc = r + dr[d], c + dc[d]
    if not (0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 0):
        d = (d + 1) % 4
        nr, nc = r + dr[d], c + dc[d]

    r, c = nr, nc

for row in arr:
    print(' '.join(map(str, row)))
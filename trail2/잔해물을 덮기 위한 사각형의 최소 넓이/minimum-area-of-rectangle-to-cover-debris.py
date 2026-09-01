x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

board = [[0] * 2000 for _ in range(2000)]

for x in range(x1 + 1000, x2 + 1000):
    board[x][y1 + 1000:y2 + 1000] = [1] * (y2 - y1)

for x in range(a1 + 1000, a2 + 1000):
    board[x][b1 + 1000:b2 + 1000] = [0] * (b2 - b1)

min_x, min_y = 2000, 2000
max_x, max_y = -1, -1

for x in range(x1 + 1000, x2 + 1000):
    row = board[x]
    if 1 not in row:
        continue
    lo = row.index(1)
    hi = len(row) - 1 - row[::-1].index(1)
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, lo)
    max_y = max(max_y, hi)

if max_x == -1:
    print(0)
else:
    print((max_x - min_x + 1) * (max_y - min_y + 1))
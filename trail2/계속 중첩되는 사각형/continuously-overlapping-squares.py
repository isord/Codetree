n = int(input())
board = [[0] * 200 for _ in range(200)]

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    color = 1 if i % 2 == 0 else 2
    for x in range(x1 + 100, x2 + 100):
        for y in range(y1 + 100, y2 + 100):
            board[x][y] = color

ans = 0
for x in range(200):
    for y in range(200):
        if board[x][y] == 2:
            ans += 1

print(ans)
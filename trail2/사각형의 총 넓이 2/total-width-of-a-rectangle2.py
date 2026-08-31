n = int(input())
board = [[0] * 200 for _ in range(200)]

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1 + 100, x2 + 100):
        for y in range(y1 + 100, y2 + 100):
            board[x][y] = 1

print(sum(map(sum, board)))
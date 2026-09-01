n = int(input())
board = [[0] * 200 for _ in range(200)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x + 100, x + 108):
        for j in range(y + 100, y + 108):
            board[i][j] = 1

print(sum(map(sum, board)))
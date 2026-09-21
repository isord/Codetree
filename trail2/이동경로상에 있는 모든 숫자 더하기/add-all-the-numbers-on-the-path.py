N, T = map(int, input().split())
cmds = input()
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y = N // 2, N // 2
d = 0
total = board[x][y]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

for c in cmds:
    if c == 'L':
        d = (d + 3) % 4
    elif c == 'R':
        d = (d + 1) % 4
    else:
        nx, ny = x + dx[d], y + dy[d]
        if in_range(nx, ny):
            x, y = nx, ny
            total += board[x][y]

print(total)
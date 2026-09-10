n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

answer = 0

for r in range(n):
    for c in range(n):
        cnt = 0
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                cnt += 1
        if cnt >= 3:
            answer += 1

print(answer)
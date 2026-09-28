R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

cnt = 0
for i in range(1, R - 1):
    for j in range(1, C - 1):
        if grid[i][j] == grid[0][0]:
            continue
        for k in range(i + 1, R - 1):
            for l in range(j + 1, C - 1):
                if grid[k][l] != grid[i][j] and grid[k][l] != grid[R-1][C-1]:
                    cnt += 1
print(cnt)
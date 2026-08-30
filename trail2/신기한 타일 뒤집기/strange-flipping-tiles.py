MAX_V = 1000 * 100 * 2
OFFSET = 1000 * 100

tiles = [-1] * (MAX_V + 1)

n = int(input())
loc = OFFSET + 1

for _ in range(n):
    x, cmd = input().split()
    x = int(x)
    if cmd == 'L':
        for i in range(loc, loc - x, -1):
            tiles[i] = 1
        loc -= x - 1
    else:
        for i in range(loc, loc + x):
            tiles[i] = 0
        loc += x - 1

white = tiles.count(1)
black = tiles.count(0)
print(white, black)

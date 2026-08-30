def solve():
    n = int(input())

    white_count = {}
    black_count = {}
    last_color = {}
    
    position = 0
    
    for _ in range(n):
        x, direction = input().split()
        x = int(x)
        
        if direction == 'R':

            for i in range(x):
                tile = position + i
                black_count[tile] = black_count.get(tile, 0) + 1
                last_color[tile] = 'B'

            position = position + x - 1
        else:

            for i in range(x):
                tile = position - i
                white_count[tile] = white_count.get(tile, 0) + 1
                last_color[tile] = 'W'

            position = position - x + 1

    all_tiles = set(white_count.keys()) | set(black_count.keys())

    white_tiles = 0
    black_tiles = 0
    gray_tiles = 0
    
    for tile in all_tiles:
        w = white_count.get(tile, 0)
        b = black_count.get(tile, 0)

        if w >= 2 and b >= 2:
            gray_tiles += 1

        elif last_color[tile] == 'W':
            white_tiles += 1
        else:
            black_tiles += 1
    
    print(white_tiles, black_tiles, gray_tiles)

solve()
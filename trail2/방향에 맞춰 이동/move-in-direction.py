n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

x, y = 0, 0
for i in range(n):
    if dir[i] == "N":
        y += dist[i]
    if dir[i] == "E":
        x += dist[i]
    if dir[i] == "S":
        y -= dist[i]
    if dir[i] == "W":
        x -= dist[i]

print(x, y, end=" ")
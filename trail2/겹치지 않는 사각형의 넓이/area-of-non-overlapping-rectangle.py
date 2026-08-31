x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())


def overlap(i):
    w = min(x2[i], x2[2]) - max(x1[i], x1[2])
    h = min(y2[i], y2[2]) - max(y1[i], y1[2])
    if w < 0:
        w = 0
    if h < 0:
        h = 0
    return w * h


ans = 0
for i in range(2):
    ans += (x2[i] - x1[i]) * (y2[i] - y1[i]) - overlap(i)

print(ans)
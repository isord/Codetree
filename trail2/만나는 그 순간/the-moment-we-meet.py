n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

def build(ds, ts):
    pos, cur = [], 0
    for direction, time in zip(ds, ts):
        step = 1 if direction == 'R' else -1
        for _ in range(time):
            cur += step
            pos.append(cur)
    return pos

a = build(d, t)
b = build(d2, t2)

answer = -1
for i in range(min(len(a), len(b))):
    if a[i] == b[i]:
        answer = i + 1
        break

print(answer)
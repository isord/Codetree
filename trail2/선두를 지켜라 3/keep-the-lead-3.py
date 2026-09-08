N, M = map(int, input().split())

v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

speed_a = []
for vi, ti in zip(v, t):
    speed_a.extend([vi] * ti)

speed_b = []
for vi, ti in zip(v2, t2):
    speed_b.extend([vi] * ti)

pos_a = pos_b = 0
prev = None
answer = 0

for sa, sb in zip(speed_a, speed_b):
    pos_a += sa
    pos_b += sb

    if pos_a > pos_b:
        cur = 'A'
    elif pos_a < pos_b:
        cur = 'B'
    else:
        cur = 'AB'

    if cur != prev:
        answer += 1
    prev = cur

print(answer)
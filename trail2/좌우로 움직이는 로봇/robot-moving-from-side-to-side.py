n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.
end = max(sum(t), sum(t_b))

ia = ib = 0
ra, rb = t[0], t_b[0]
diff = 0
answer = 0

for _ in range(end):
    prev = diff

    if ia < n:
        diff += 1 if d[ia] == 'R' else -1
        ra -= 1
        if ra == 0:
            ia += 1
            if ia < n:
                ra = t[ia]

    if ib < m:
        diff -= 1 if d_b[ib] == 'R' else -1
        rb -= 1
        if rb == 0:
            ib += 1
            if ib < m:
                rb = t_b[ib]

    if diff == 0 and prev != 0:
        answer += 1

print(answer)
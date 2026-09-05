n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

sa = []
for i in range(n):
    sa.extend([v[i]] * t[i])

sb = []
for i in range(m):
    sb.extend([v2[i]] * t2[i])

pa = pb = 0
prev = 0 
count = 0

for i in range(len(sa)):
    pa += sa[i]
    pb += sb[i]

    if pa > pb:
        cur = 1
    elif pa < pb:
        cur = -1
    else:
        cur = 0

    if cur != 0:
        if prev != 0 and cur != prev:
            count += 1
        prev = cur

print(count)
N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

infected = [False] * (N + 1)
remain = [0] * (N + 1)

infected[P] = True
remain[P] = K

handshakes.sort()

for t, x, y in handshakes:
    active_x = infected[x] and remain[x] >= 1
    active_y = infected[y] and remain[y] >= 1

    if active_x:
        remain[x] -= 1
    if active_y:
        remain[y] -= 1

    if active_x and not infected[y]:
        infected[y] = True
        remain[y] = K
    if active_y and not infected[x]:
        infected[x] = True
        remain[x] = K

print(''.join('1' if infected[i] else '0' for i in range(1, N + 1)))
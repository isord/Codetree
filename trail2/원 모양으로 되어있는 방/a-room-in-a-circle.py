n = int(input())
a = [int(input()) for _ in range(n)]

answer = float('inf')

for start in range(n):
    total = 0

    for distance in range(n):
        room = (start + distance) % n
        total += a[room] * distance

    answer = min(answer, total)

print(answer)
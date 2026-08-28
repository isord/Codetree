n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

line = [0] * 101

for start, end in segments:
    for i in range(start, end+1):
        line[i] += 1

print(max(line))
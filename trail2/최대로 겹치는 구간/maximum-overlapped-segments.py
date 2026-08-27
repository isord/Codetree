n = int(input())

segments = [tuple(map(int, input().split())) for _ in range(n)]

min_value = min(min(start, end) for start, end in segments)
max_value = max(max(start, end) for start, end in segments)

arr = [0] * (max_value - min_value)

for start, end in segments:
    for i in range(start, end):
        arr[i - min_value] += 1

print(max(arr))
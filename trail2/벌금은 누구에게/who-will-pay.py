N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

count = [0] * (N + 1)
answer = -1

for a in student:
    count[a] += 1
    if count[a] == K:
        answer = a
        break

print(answer)
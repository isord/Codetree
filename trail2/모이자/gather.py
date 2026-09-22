n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
min_sum = 10000000
for i in range(n):
    sum_diff = 0
    standard = i
    for j in range(n):
        sum_diff += abs(i - j) * A[j]

    min_sum = min(min_sum, sum_diff)

print(min_sum)
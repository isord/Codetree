a, b, c = map(int, input().split())

# Please write your code here.
day = 11
hour = 11
min = 11

elapsed_time = 0

if (a, b, c) < (11, 11, 11):
    print(-1)
else:
    while True:
        if day == a and hour == b and min == c:
            break

        elapsed_time += 1
        min += 1

        if min == 60:
            hour += 1
            min = 0

        if hour == 24:
            day += 1
            hour = 0

    print(elapsed_time)
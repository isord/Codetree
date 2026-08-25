m1, d1, m2, d2 = map(int, input().split())
A = input()

month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

elapsed_day = 0
while True:
    if m1 == m2 and d1 == d2:
        break
    
    elapsed_day += 1
    d1 += 1

    if d1 > month[m1]:
        m1 += 1
        d1 = 1


if A == 'Mon':
    print(elapsed_day//7 + 1)
if A == 'Tue':
    if (elapsed_day % 7) >= 1:
        print(elapsed_day//7 + 1)
    else:
        print(elapsed_day//7)
if A == 'Wed':
    if (elapsed_day % 7) >= 2:
        print(elapsed_day//7 + 1)
    else:
        print(elapsed_day//7)
if A == 'Thu':
    if (elapsed_day % 7) >= 3:
        print(elapsed_day//7 + 1)
    else:
        print(elapsed_day//7)
if A == 'Fri':
    if (elapsed_day % 7) >= 4:
        print(elapsed_day//7 + 1)
    else:
        print(elapsed_day//7)
if A == 'Sat':
    if (elapsed_day % 7) >= 5:
        print(elapsed_day//7 + 1)
    else:
        print(elapsed_day//7)
if A == 'Sun':
    if (elapsed_day % 7) >= 6:
        print(elapsed_day//7 + 1)
    else:
        print(elapsed_day//7)
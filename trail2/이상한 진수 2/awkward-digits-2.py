a = list(input())
answer = 0

for i in range(len(a)):
    original = a[i]

    # 현재 자리만 뒤집기
    if a[i] == '0':
        a[i] = '1'
    else:
        a[i] = '0'

    value = int(''.join(a), 2)
    answer = max(answer, value)

    a[i] = original

print(answer)
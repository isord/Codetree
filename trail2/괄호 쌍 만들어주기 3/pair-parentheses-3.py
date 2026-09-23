A = input()

open_count = 0
answer = 0

for c in A:
    if c == '(':
        open_count += 1
    else:
        answer += open_count

print(answer)
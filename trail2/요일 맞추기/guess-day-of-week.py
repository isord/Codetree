m1, d1, m2, d2 = map(int, input().split())

days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_of_week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

def day_of_year(month, day):
    return sum(days_in_month[1:month]) + day

day1 = day_of_year(m1, d1)
day2 = day_of_year(m2, d2)
diff = day2 - day1

result_index = (1 + diff) % 7

print(days_of_week[result_index])
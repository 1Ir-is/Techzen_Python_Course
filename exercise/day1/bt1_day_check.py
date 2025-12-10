def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def max_day(month, year):
    if month == 2:
        return 29 if is_leap(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 0

def is_valid(day, month, year):
    if year < 1 or month < 1 or month > 12:
        return False
    return 1 <= day <= max_day(month, year)

def next_day(day, month, year):
    day += 1
    if day > max_day(month, year):
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    return day, month, year

def prev_day(day, month, year):
    day -= 1
    if day < 1:
        month -= 1
        if month < 1:
            month = 12
            year -= 1
        day = max_day(month, year)
    return day, month, year

# Nhập thông tin từ bàn phím
d = int(input("Nhập ngày: "))
m = int(input("Nhập tháng: "))
y = int(input("Nhập năm: "))

if not is_valid(d, m, y):
    print("Ngày không hợp lệ")
else:
    n_d, n_m, n_y = next_day(d, m, y)
    p_d, p_m, p_y = prev_day(d, m, y)
    print(f"Ngày kế tiếp: {n_d}/{n_m}/{n_y}")
    print(f"Ngày trước đó: {p_d}/{p_m}/{p_y}")
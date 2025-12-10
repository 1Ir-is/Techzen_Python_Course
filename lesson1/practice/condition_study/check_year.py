try:
    year = int(input("Enter year: "))
    is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
    print("Leap" if is_leap else "Not Leap")
except ValueError:
    print("Invalid input")

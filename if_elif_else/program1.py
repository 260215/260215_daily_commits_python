# Write a Python program to get next day of a given date using if-elif-else
def next_day(year, month, day):
    if year % 400 == 0:
        leap_year = True
    elif year % 100 == 0:
        leap_year = False
    elif year % 4 == 0:
        leap_year = True
    else:
        leap_year = False

    if month in (1, 3, 5, 7, 8, 10, 12):
        month_length = 31
    elif month == 2:
        if leap_year:
            month_length = 29
        else:
            month_length = 28
    else:
        month_length = 30

    if day < month_length:
        day += 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1

    print("The next day is %d: " % (day))


if __name__ == '__main__':
    year = int(input("Enter a year : "))
    month = int(input("Enter a month[1-12] : "))
    day = int(input("Enter a day[1-31] : "))
    next_day(year, month, day)

# write a program to check if a given year is a leap year.

year = int(input('input your year '))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('leap year')
        else:
            print('not leap year')
    else:
        print('leap year')
else:
    print('not leap year')

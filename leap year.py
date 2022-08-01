# write a program to check if a given year is a leap year.

leap_year = int(input('what year would you like to check? '))
if leap_year % 4 == 0 and leap_year % 100 != 0:
    print('this is a leap year')
elif leap_year % 100 == 0:
    print("this is a not leap year")
elif leap_year % 400 == 0:
    print('this is a leap year')
else:
    print('this is not a leap year')

# write a program to check if a given year is a leap year.

year = int(input('what year do you want to check? '))
if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
    print('this is a leap year')
else:
    print('this is not a leap year')

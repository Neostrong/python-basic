# roller coaster ride

height = int(input('what is your height? '))
bill = 0
if height > 120:
    print('you can ride the roller coaster, only if you are old enough')
    age = int(input('how old are you? '))
    if age < 12:
        bill = 5
        print(f'kids tickets cost ${bill} ')
    elif age < 18:
        bill = 7
        print(f'youths ticket cost ${bill}')
    else:
        bill = 12
        print(f'adult tickets cost ${bill}')
    photo = input('do you want your photos taken? yes or no : ')
    if photo == 'y':
        bill += 3
        print(f'your bill with photo is ${bill} ')
    else:
        print(f"your bill without photo is ${bill}")
else:
    print('you cannot ride the roller coaster')

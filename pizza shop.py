# automated pizza hut

print("hello, welcome to pizza hut.")
size = input('what size of pizza do you want? ')
add_pepperoni = input('do you want pepperoni?  ')
extra_cheese = input('what about extra cheese? ')

bill = 0

if size == 's':
      bill += 15
elif size == 'm':
      bill += 20
elif size == 'l':
      bill += 25

if add_pepperoni == 'y':
      if size == 's':
            bill += 2
      else:
            bill += 3

if extra_cheese == 'y':
      bill += 1
else:
      bill += 0

print(f'your bill is ${bill}')
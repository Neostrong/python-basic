print('welcome to tip calculator')
bill = input('what was the total bill? ')
tip = input('what percentage tip would you like to give? 10, 12 or 15? ')
percent_tip = (int(tip) * float(bill))/100
n_persons = input('how many people to split the bill? ')
amount =(float(bill) + float(percent_tip))/int(n_persons)
print(f'each person should pay: {round(amount, 2)}')
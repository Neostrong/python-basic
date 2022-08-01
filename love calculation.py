# love calculator

print('welcome to love calculator!')
name1 = input('what is your name? ')
name2 = input('what is their name?')
both_names = name1 + name2
name = both_names.lower()

t = name.count('t')
r = name.count('r')
u = name.count('u')
e = name.count('e')

l = name.count('l')
o = name.count('o')
v = name.count('v')
e = name.count('e')

a = t+r+u+e
b = l+o+v+e

st = (str(a) + str(b))
s = int(st)
if s < 10 or s > 90:
    print(f'your score is {s}, you go together like coke and mentos')
elif s > 40 and s < 50:
    print(f'your love score is {s},you are alright together')



# write a program to calculate the body mass index:

weight = input('what is your weight in kilogram? ')
height = input('what is your height in metres? ')
print('From your inputs, your body mass index is ')
bmi = float(weight) / float(height)**2
print(int(bmi))
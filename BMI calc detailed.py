# Body mass index calculator with details

mass = float(input("what is your mass? "))
height = float(input("what is your height? "))
mass_index = mass / height**2
bmi = int(mass_index)
if bmi < 18.5:
    print(f'your bmi is {bmi}, you are underweight')
elif bmi < 25:
    print(f'your bmi is {bmi}, you have normal weight')
elif bmi < 30:
    print(f'your bmi is {bmi}, you are over weight')
elif bmi < 35:
    print(f'your bmi is {bmi}, i am so sorry, you are obese')
else:
    print(f'your bmi is {bmi}, wow you are clinically obese')
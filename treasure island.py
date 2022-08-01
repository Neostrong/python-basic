print('welcome to treasure island')
choice1 = input("where do u want to, 'left' or 'right'?  ").lower()
if choice1 == 'left':
    print('continue')
    choice2 = input("do u want to 'wait' or 'swim'? ").lower()
    if choice2 == 'wait':
        print('which door')
        choice3 = input("you have to choose between the 'blue', 'red' or 'yellow'  ").lower()
        if choice3 == 'yellow':
            print('you win')
        elif choice3 == 'red':
            print('you dead, game over')
        elif choice3 == 'blue':
            print('death by vampire, game over')
        else:
            print('game over, the door does not exist')
    else:
        print('game over, you were bitten by sharks!')
else:
    print('game over, you fell into a hole')

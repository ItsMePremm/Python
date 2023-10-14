import random

choose = ['Rock', 'Paper', 'Scissor']

print('\tWelcome to RPS')
m = 'Type R for Rock, P for Paper, and S for Scissor'
print(m)
uwin = 0
comwin = 0
draw  = 0
for i in range(0, 10):
    while True:
        try:
            print('Enter Your Choice')
            c = input().upper()

            if c in ('R', 'P', 'S'):
                break
            else:
                raise ValueError('Invalid choice. Please enter R, P, or S.')

        except ValueError as e:
            print(e)

    value = choose[0] if c == 'R' else choose[1] if c == 'P' else choose[2]
    ran = random.choice(choose)

    print(f'You Choose {value} and Computer Choose {ran}')
    if value == ran:
        print('Draw')
        draw = draw + 1
    elif value == choose[0] and ran == choose[1]:
        print('Computer Won You Lose')
        comwin = comwin +1
    elif value == choose[1] and ran == choose[0]:
        print('You Won Computer lose')
        uwin = uwin + 1
    elif value == choose[0] and ran == choose[2]:
        print('You Won Computer lose')
        uwin = uwin + 1
    elif value == choose[2] and ran == choose[0]:
        print('Computer Won You Lose')
        comwin = comwin + 1
    elif value == choose[1] and ran == choose[2]:
        print('Computer Won You Lose')
        comwin = comwin + 1
    elif value == choose[2] and ran == choose[1]:
        print('You Won Computer lose')
        uwin = uwin + 1
print(f'You won {uwin} times, Computer Won {comwin} and Draw occur {draw} times.\nThanks for playing.r ')
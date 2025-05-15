import random
a=['rock','paper','scissors']
c=0
u=0
while max(c,u)<5:
    b=random.choice(a)
    t=input()
    if b==a[0]:
        if t==a[1]:
            u+=1
            print('You win')
        elif t!=a[0]:
            c+=1
            print('Computer win')
        else:
            print('Tie')
    elif b==a[1]:
        if t==a[2]:
            u+=1
            print('You win')
        elif t!=a[1]:
            c+=1
            print('Computer win')
        else:
            print('Tie')
    elif b==a[2]:
        if t==a[0]:
            u+=1
            print('You win')
        elif t!=a[2]:
            c+=1
            print('Computer win')
        else:
            print('Tie')
if u>c:
    print('You win the game over')
else:
    print('You lost the game over')
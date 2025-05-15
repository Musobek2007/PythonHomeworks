from random import*
while 1:
    f=0
    a=randint(1,100)
    i=0
    while i<10:
        b=int(input())
        if b>a:
            print('Too high!')
        elif b<a:print('Too low!')
        else:
            f=1
            print('You guessed it right!')
            break
        i+=1
    if f:
        break
    else:
        print('You lost. Want to play again?')
        g=input().lower()
        if g not in ['y','yes','ok']:
            break

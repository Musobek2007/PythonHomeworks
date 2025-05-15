a=input()
n=len(a)
if n<8:
    print('Password is too short.')
elif a==a.lower():
    print('Password must contain an uppercase letter.')
else:print('Password is strong.')
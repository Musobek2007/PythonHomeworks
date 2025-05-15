import random
import math
def is_prime(n):
    if n<=1:return False
    if n<=3:return True
    if n%2==0:return False
    r,d=0,n-1
    while d%2==0:
        d//=2
        r+=1
    for i in range(5):
        a=random.randint(2,n-2)
        x=pow(a,d,n)
        if x==n-1 or x==1:
            continue
        for j in range(r-1):
            x=pow(x,2,n)
            if x==n-1:
                break
        else:
            return False
    return True
try:
    n=int(input())
    print(is_prime(n))
except:
    print('enter only integers')
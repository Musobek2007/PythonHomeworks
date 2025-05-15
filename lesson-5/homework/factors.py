try:
    n=int(input('Enter a positive integer: '))
    p=[]
    for j in range(1,int(n**0.5)+1):
        if n%j==0:
            p+=[j]
            if n//j!=j:
                p+=[n//j]
    p.sort()
    for i in p:
        print(i,'is a factor of',n)
except:
    print('Enter a positive integer')
txt=input()
d='euioaEUIOA'
s=''
k=1
for i in txt:
    if k%3==0:
        if i in d:
            s+=i
            k-=1
        else:
            s+=i+'_'
    else:s+=i
    k+=1
print(s[:-1] if s[-1]=='_' else s)

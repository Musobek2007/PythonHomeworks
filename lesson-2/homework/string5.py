a=input().lower()
b='aeoiu'
s=0
for j in b:
    s+=a.count(j)
n=0
for i in a:
    if i.isalpha():n+=1
print(s,n-s)

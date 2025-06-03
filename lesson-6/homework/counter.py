from collections import*
with open('sample.txt') as file:
    txt=file.readlines()
lis=[]
for i in txt:
    g=i.lower()
    for j in '.,!?':
        g=g.replace(j,'')
    g=g.split()
    lis.extend(g)
p=Counter(lis)
lis=list(set(lis))
lis.sort(key=lambda x:p[x],reverse=1)
rank=int(input('Enter number of top common words: '))
print('Total words:',len(lis))
print('Top',rank,'most common words:')
n=0
for i in lis:
    if n>=rank:break
    print(i,'-',p[i],'times')
    n+=1
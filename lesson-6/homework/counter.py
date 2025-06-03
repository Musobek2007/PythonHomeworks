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
txt=open('word_count_report.txt','w')
print('Total words:',len(lis))
txt.write('Total words: '+str(len(lis)))
print('Top',rank,'most common words:')
txt.write('\n')
txt.write('Top '+str(rank)+' most common words:')
txt.write('\n')
n=0
for i in lis:
    if n>=rank:break
    print(i,'-',p[i],'times')
    txt.write(i+'-'+str(p[i])+' times')
    txt.write('\n')
    n+=1
txt.close()
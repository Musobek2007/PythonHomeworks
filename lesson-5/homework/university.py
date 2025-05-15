s=[]
list1=[]
list2=[]
yi_l1=0
yi_l2=0
le=0
print('******************************')
def enrollment_stats():
    totl_stud=0
    totl_fee=0
    global le,yi_l1,yi_l2
    while 1:
        a=input().split()
        if len(a)==0:
            break
        else:
            s.append(a)
            totl_stud+=int(a[1])
            totl_fee+=int(a[2])
            list1.append(int(a[1]))
            yi_l1+=int(a[1])
            list2.append(int(a[2]))
            yi_l2+=int(a[2])
            le+=1
    print('Total students:',totl_stud)
    print('Total tuition: $',totl_fee)
enrollment_stats()
print()
list1.sort()
list2.sort()
def mean(list1):
    print('Student mean:',format(yi_l1/le,'.2f'))
mean(list1)
def median(list1):
    if le%2:
        print('Student median:',list1[le//2])
    else:
        print('Student median:',(list1[le//2]+list1[le//2-1])/2)
median(list1)
print()
print('Tuition mean: $',format(yi_l2/le,'.2f'))
if le%2:
    print('Tuition median: $',list2[le//2])
else:
    print('Tuition median: $',(list2[le//2]+list2[le//2-1])/2)
print('******************************')
a=tuple(map(int,input().split()))
c=int(input())
b=tuple([i]*c for i in a)
print(b)
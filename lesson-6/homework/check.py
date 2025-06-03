def check(func):
    def di(a,b):
        try:
            print(func(a,b))
        except ZeroDivisionError:
            print('Denominator can\'t be zero')
    return di
@check
def div(a,b):
    return a/b
try:
    a,b=map(int,input().split())
    div(a,b)
except:
    print('Enter only digits')
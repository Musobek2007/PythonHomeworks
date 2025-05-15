def invest(amount,rate,years):
    for i in range(years):
        amount=amount*(1+rate)
        print('year '+str(i+1)+': $'+str(format(amount,'.2f')))
try:
    amount,rate,years=map(float,input().split())
    invest(amount,rate,int(years))
except:
    print('Write number only')
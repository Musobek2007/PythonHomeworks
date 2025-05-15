def convert_cel_to_far():
    F=float(input('Enter a temperature in degrees F:'))
    C=(F-32)*5/9
    print(str(F)+' degrees F =',format(C,'.2f'),'degrees C')
convert_cel_to_far()
print()
def convert_far_to_cel():
    C=float(input('Enter a temperature in degrees C:'))
    F=C * 9/5 + 32
    print(str(C)+' degrees C =',format(F,'.2f'),'degrees F')
convert_far_to_cel()
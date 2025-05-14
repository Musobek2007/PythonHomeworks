a={'a': 1, 'b': 2, 'c': 3}
b={'c': 30, 'd': 4, 'e': 5}
c=set(a.keys()) & set(b.keys())
print(c)         
print(bool(c))


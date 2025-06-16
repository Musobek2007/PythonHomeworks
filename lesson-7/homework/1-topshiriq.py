class Vector:
    def __init__(self,points):
        self.points=points
    def __add__(self,other):
        if len(self.points)==len(other.points):
            new_ve=[]
            for i in range(len(self.points)):
                new_ve.append(self.points[i]+other.points[i])
            return Vector(new_ve)
        else:
            return 'Enter vectors with the same lenght'
    def __str__(self):
        return 'Vector('+', '.join(map(str,self.points))+')'
    def __sub__(self,other):
        if len(self.points)==len(other.points):
            new_ve=[]
            for i in range(len(self.points)):
                new_ve.append(self.points[i]-other.points[i])
            return Vector(new_ve)
        else:
            return 'Enter vectors with the same lenght'
    def __mul__(self,other):
        try:
            return Vector([int(other)*i for i in self.points])
        except:
            if len(self.points)==len(other.points):
                dot=0
                for i in range(len(self.points)):
                    dot+=self.points[i]*other.points[i]
                return dot
            else:
                return 'Enter vectors with the same lenght'
    def __rmul__(self,other):
        return self.__mul__(other)
    def magnitude(self):
        yi=0
        for i in self.points:yi+=i**2
        return yi**0.5
    def normalize(self):
        yi=0
        for i in self.points:yi+=i**2
        mag=yi**0.5
        new_ve=[format(i/mag,'.3f') for i in self.points]
        return Vector(new_ve)
v1=Vector(list(map(int,input().split())))
v2=Vector(list(map(int,input().split())))
print(v1)
v3=v1+v2
print(v3)
v4=v2-v1
print(v4)
dot=v1*v2
print(dot)
v5=3*v1
print(v5)
print(v1.magnitude())
print(v1.normalize())


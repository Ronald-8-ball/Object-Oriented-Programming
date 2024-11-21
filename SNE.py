class parrot :
    specie = "bird"
    def __init__(self,name,age) :
     self.name = name
     self.age  = age
obj = parrot("Roy",1)
print(obj.specie)
print(obj.name)
print(obj.age)
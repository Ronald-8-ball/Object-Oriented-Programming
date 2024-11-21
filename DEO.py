class student :
    grade = 11
    name = "Steve"
    def introduction(self) :
     print("Introducing my self")
    def details(self) :
     print("I'm in grade",self.grade,"My name is",self.name)
obj = student()
obj.introduction()
obj.details()

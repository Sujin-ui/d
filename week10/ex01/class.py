class student:  
    def __init__(self, name="무명씨", age=20):  
        self.name  = name
        self.age = age
        
stu1 = student( )
print(stu1.name, stu1.age)

stu2 = student()
stu2.name ="kim inha"
stu2.age = 20
print(stu2.name, stu2.age)
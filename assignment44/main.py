class Student:
    usertype = "Student"#class attribute
    
    def __init__(self, name, age):
        #constructor
        self.name = name# instance attributee
        self.age = age# instance attributee
    
    def printObject(self):
        return f"Name: {self.name} Age: {self.age}"  
    
    def greet(self, msg):
        return f"{msg} {self.name}"
    
    def __str__(self):# similar to toString in Java
        return f"Name: {self.name} Age: {self.age}"  


obj1 = Student("Prasanth",34)
print(obj1.printObject())
print(obj1.greet("Hi"))
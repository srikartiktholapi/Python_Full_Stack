# -------------------------------
# Example 1 : Basic Constructor
# -------------------------------

class NewClass:
    def __init__(self):
        print("i am getting executed")
        self.a = 90
        self.b = 78
    
    def add(self):
        return self.a + self.b


obj = NewClass()
print(obj.add())   # 168



# -------------------------------
# Example 2 : Class vs Instance Variables
# -------------------------------

class Student:
    a = 90                  # class variable

    def __init__(self, name):
        self.name = name    # instance variable
        print("i am getting executed")
        self.b = 78         # instance variable
    
    def add(self):
        return self.a + self.b


# First object
obj = Student("default")
print(Student.a)            # 90

# Changing class variable
Student.a = 67

# Alice object
Alice = Student("Alice")
print(Alice.a)              # 67
Alice.b = 34
print(Alice.b)              # 34
print(Alice.add())          # 101

# Ajay object
Ajayobj = Student("Ajay")
print(Ajayobj.a)            # 67
print(Ajayobj.add())        # 145



# -------------------------------
# Example 3 : Person Class
# -------------------------------

class Person:
    name = "name"     # class variable
    age = 14          # class variable

    def sleep(self):
        print("sleeping executed")


# Object 1
personObj1 = Person()
personObj1.name = "ajay"
personObj1.age = 24
print(personObj1.age)       # 24

# Object 2
personObj2 = Person()
personObj2.name = "vijay"
personObj2.age = 34
print(personObj2.age)       # 34

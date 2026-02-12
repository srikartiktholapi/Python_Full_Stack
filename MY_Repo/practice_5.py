#Q1
class addition_calucator :
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

obj1=addition_calucator("Tesla","CyberTruck")
obj2=addition_calucator("Tata","Nexon")
print(obj1.brand,"------>",obj1.model)
print(obj2.brand,"------>",obj2.model)
#Q2
class Box() :
    def area(self,width,height):
        return width * height
    
obj3=Box()
print(obj3.area(7,3))
#Q3
class student():
    def greet(self,name):
        self.name =name
        return f"hello-->{self.name}"

obj5=student()
obj6=student()
print(obj5.greet("satya"))
print(obj6.greet("srikartik"))
#Q4
class Laptop():
    def specfication(self,RAM,price):
        self.RAM=RAM
        self.price=price
        return f"this RAM{self.RAM},and the price is {self.price}"

obj7=Laptop()
obj9=Laptop()
print(obj7.specfication("16 GB","45000"))
print(obj9.specfication("8GB","90000"))
#Q5
class Bank_Account():
    def __init__(self):
        self.balance =0
    def deposit(self,amount):
        self.balance+=amount
        return f"Therefore after deposit you're balance amount --->{self.balance}"
obj10=Bank_Account()
obj11=Bank_Account()
print(obj10.deposit(12000))
print(obj11.deposit(1000))
print(obj10.deposit(12))
#Q6
class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self) :
        print(self.x,self.y)

p1 = Point(3, 4)
p2 = Point(10, 20)

p1.show()   
p2.show()   
#Q7
class computer():
    def specfication(self,RAM,price):
        self.RAM=RAM
        self.price=price
        return f"this RAM{self.RAM},and the price is {self.price}"

obj12=computer()
obj13=computer()
print(obj12.specfication("16 GB","45000"))
print(obj13.specfication("8GB","90000"))
obj12.RAM = " 32GB"
obj13.RAM ="64GB"
print(obj12.RAM)
print(obj13.RAM)
class Number :
    a =12
    def first_number(self,b) :
         self.b =b
         print("i am getting executed",self.b)

    def add(self):
        return self.a+self.b

num=Number()
print(Number.a)
num.first_number(8)   
print(num.add())
Number.a =1
print(Number.a)
num.b=9
print(num.b)









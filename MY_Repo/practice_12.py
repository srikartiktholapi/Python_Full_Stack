class Automobile :
    def __init__(self):
        print("contructor of the class Automobile intialized")
    def move(self):
        print("the vechile started moving ")    

obj1 = Automobile()
obj1.move()
# a= int(input("enter the number"))
# b= int(input("enter the second number"))
# result = a+b
# print(result)
# result = a-b
# print(result)
# result = a*b
# print(result)
# result = a**b
# print(result)
# result = a%b
# print(result)

a = True
b = False
resultAND = a and b 
resultOR = a or b 

print(resultAND)
print(resultOR)
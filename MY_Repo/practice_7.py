class student :
    def __init__(self,name,id):
        self.name =name
        self.id=id

    def printing_details(self):
        print(self.name)
        print(self.id)

s1 =student("sri kartik","21")
s1.printing_details()

class person :
    name ="sri Kartik"
    roll_no = 34
    def printing(self):
        print(self.name)
        print(self.roll_no)
s1 = person()
s2=s1
s1.printing()
s2.printing()
import copy

s3 =copy.copy(s1)
s1.printing()
s3.printing()
s3.roll_no=21
print(s3.roll_no)
print(s1.__doc__)

            
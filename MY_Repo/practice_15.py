class Logical_Operator :
    def comparision(self,a,b):
        if (a < 18 and b < 18):
            print("A and B are not eligible Voters")
        elif (18<a<60 and 18<b<60) :
            print ("A and B are adults")
        elif (a < 18 or b < 18):
            print ("Among A and B one is minor")
        else :
            pass

obj1 = Logical_Operator()
obj1.comparision(1,2)
# in comprassion operator 
name_1 = "Tholapi Sri Kartik"
print('Z'in name_1)
if 'K' in name_1 :
    print("K is in name_1")
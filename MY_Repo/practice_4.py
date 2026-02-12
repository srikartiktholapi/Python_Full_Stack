class Dog :
    def __init__(self,branch :str,fuel_type :str)->None :
        self.branch =branch
        self.fuel_type=fuel_type
    def speak(self):
        print("I am",self.branch,"and my fuel type is",self.fuel_type)    
d1=Dog("volwo","dissel")
d2=Dog("nano","petrol")

d1.speak()
d2.speak()

"""
MY_Repo.practice_14
date : 15-12-2025"""
Voter_age = int(input("Enter the voter age :"))
if Voter_age <18 :
    print("This voter is not eligible for voting ")
elif Voter_age >=18 | Voter_age < 60:
    print("Voter is an eligible man and don't require assistance")
else :
    print("Voter is a senior citizen who need assistence")        

# loop 
names =['sri kartik','Tholapi Sri Kartik','Satya','Tholapi Satya']
for name in names :
    print(name)
for i in range(1,100,2) :
    print(i)

for i in range(1,10):
    if i == 7:
        print("Found it",i)
        break 
    print(i)     
else:
    print("loop exceuted successfully")    

#check if a number is prime or not if not printing it's factors 

for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n,"equals",x,"*",n//x)
            break 
    else :
        print(n ," is a prime number")        

#pass keyword 
def math() :
    """This code is used for maths operations """
    pass 
def add(a,b):
    c=a+b
    print(c)
    pass

add(10,20)
print(math.__doc__)
"""
continue keyword usage 
"""
for i in range(1,10):
    if (i==5):
        continue
    print(i)
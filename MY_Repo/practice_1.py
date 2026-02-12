print("select which operation would you like to perform")
print("1.Addition")
print("2.subtraction")
print("3.Multiplication")
print("4.division")
Selection_number =input("select the serial number of the operation you would like to perform ?")
number1=int(input("enter the first number :"))
number2=int(input("enter the second number :"))

if Selection_number == "1" :
    print("addition =",number1+number2)
elif Selection_number=="2" :
    print("subtraction =",number1-number2)
elif Selection_number=="3" :
    print("Multiplication =",number1*number2)
else :
    if number2==0 :
        print("Not possible") 
    else :
        print("division =",number1/number2)      

    
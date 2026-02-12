import requests

Name   =input("Enter You're Name :")
Weight =int(input("Enter You're Weight :"))
Height_feet =float(input("Enter You're Height (feet) :"))
In_meters =Height_feet * 0.3048
response = requests.get(f"https://bmicalculatorapi.vercel.app/api/bmi/{Weight}/{In_meters}")
data = response.json()
print("Category you belong :" + data['Category'].upper() )
In_feet = data['height']*3.28084
print("You're height :"+ str(In_feet))

print("You're weight :"+ str(data['weight']))
print("Body mass Index(BMI) "+str(data['bmi']))

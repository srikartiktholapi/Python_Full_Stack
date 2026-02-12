import requests
import json 

name =input("enter the name of the person :")

response = requests.get(f"https://api.genderize.io?name={name}")
data = response.json()
print(json.dumps(data,indent=2))

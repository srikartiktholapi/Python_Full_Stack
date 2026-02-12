import requests
import json

words =input("enter the word : ")

response =requests.get(f"https://api.datamuse.com/words?sl={words}")
data=response.json()
print(data)
for item in data :
    print(item["word"])
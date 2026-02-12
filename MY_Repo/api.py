import requests

st = input("enter the starting data")
ed = input("enter the ending data")

res = requests.get(f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={st}&endtime={ed}&minmagnitude=5")
data = res.json()
print(data)
#2023-03-01
#2023-03-02
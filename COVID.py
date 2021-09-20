import requests
from tkinter import *


url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"

headers = {
    'x-rapidapi-key': "3b6b9c60b2mshef89cf1e6eaa609p1835d5jsn6f3ccbfcf3a9",
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)
info=response.json()

place=info['state_wise']
state=place['Maharashtra']
dist=state['district']
city=dist['Pune']
active=city['active']
confirmed=city['confirmed']
deceased=city['deceased']
recovered=city['recovered']

print("STATE: MAHARASHTRA")
print("CITY: PUNE")
print("ACTIVE CASES:",active)
print("CONFIRMED CASES:",confirmed)
print("RECOVERED:",recovered)
print("DEATHS:",deceased)

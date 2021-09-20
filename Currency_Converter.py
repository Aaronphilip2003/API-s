import requests

url = "https://currency-exchange.p.rapidapi.com/exchange"

to=input("Which currency do you want to convert to:")
from1=input("Which currency do you want to convert from:")



querystring = {"to":to,"from":from1,"q":"1.0"}

headers = {
    'x-rapidapi-key': "API KEY",
    'x-rapidapi-host': "currency-exchange.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

ans=response.text

floatANS=(float)(ans)

amount=input("What is the amount you want to convert:")
amountFLOAT=(float)(amount)

print("The amount according to today's conversion rate is:",amountFLOAT*floatANS,to)


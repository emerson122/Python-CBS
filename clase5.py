import requests

response = requests.get("http://api.weatherapi.com/v1/current.json?key=91dcf5931cde409d852180755222106&q=London&aqi=no")
print(response)
respuesta = response.json()
# print(respuesta)
print(respuesta['location']['name'],respuesta['location']['lat'])

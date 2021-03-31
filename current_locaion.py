import requests

r = requests.get('http://easiway.in/')

ip_request = requests.get('http://easiway.in/ip.json')
ip_add = ip_request.json()['ip']
print(ip_add)

url = 'http://easiway.in/ip.json'+ip_add+'.json'

geo_request = requests.get(url)
geo_data = requests.json()
print(geo_data)

print(geo_data['latitude'])
print(geo_data['longitude'])

print(geo_data['city'])
print(geo_data['region'])
print(geo_data['country'])
print(geo_data['timezone'])

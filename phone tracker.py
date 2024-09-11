import phonenumbers
from phonenumbers import carrier
import opencage
from opencage.geocoder import OpenCageGeocode
import folium
phonenumber=str(input("Enter your number:"))
pepnumber=phonenumbers.parse(phonenumber)
print(location)
service_pro=phonenumbers.parse(phonenumber)
print(carrier.name_for_number(service_pro,"en"))
key='19edc2add36146c49a2b4ae57e0580a7'

geocoder= OpenCageGeocode(key)
query=str(location)
results=geocoder.geocode(query)
print(results)
let=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
print(lat,lag)
myMap=folium.Map(location=[lat,lng,zoom_start== 9])
folium.Marker([lat,lng],popup=location).add_to(myMap)
myMap.save("mylocation.html")
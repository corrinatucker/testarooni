from geopy.geocoders import Nominatim
from geopy.distance import vincenty

geolocator = Nominatim()
location = geolocator.geocode("175 5th Avenue NYC")
print(location.address)
print((location.latitude, location.longitude))
print(location.raw)

location = geolocator.reverse("40.7411, -73.9897")
print(location.address)
print((location.latitude, location.longitude))
print(location.raw)

flat_iron = (41.49008, -71.312796)
psb = (42.119308, -79.983714)
print(vincenty(flat_iron, psb).miles)


#https://github.com/geopy/geopy
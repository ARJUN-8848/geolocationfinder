
import geocoder
import reverse_geocoder as rg

def find_geolocation():
    latitude, longitude = geocoder.ip("me").latlng
    print(latitude, longitude)
    city = rg.search((latitude, longitude), verbose=False)
    return city[0]["name"]

if __name__ == "__main__":
    print(find_geolocation())

# import swapi
import requests
# from PIL import Image
import webbrowser
from datetime import datetime

res = requests.get('https://scotch.io')

print(res)

image_url = 'https://http.cat/' + str(res.status_code)

print(image_url)
# webbrowser.open(image_url)

# city_request = requests.get(f'https://www.metaweather.com/api/location/search/?query={city}')
# if city_request.status_code == 200:
#     city_data = city_request.json()
#     city_id = city_data[0]['woeid']
# else:
#     print("Huston, we have a problem")


# with Image.open('C:\Users\starostina\Pictures\Boris-A2-Deutch.bmp') as img:
#     img.show()

swapi_res = requests.get('https://swapi.dev/api/planets/1')
swapi_data = swapi_res.json()
print(swapi_data)

# pm = swapi.get_film(4)
# jj = swapi.get_person(36)
# for c in pm.get_characters().iter():
#     if c.name == jj.name:
#         print("Why George, why.")
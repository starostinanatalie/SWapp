import swapi
import requests
from PIL import Image
import webbrowser


res = requests.get('https://scotch.io/life')

print(res)

image_url = 'https://http.cat/' + str(res.status_code)

print(image_url)
webbrowser.open(image_url)

# with Image.open('C:\Users\starostina\Pictures\Boris-A2-Deutch.bmp') as img:
#     img.show()

swapi_res = requests.get('https://swapi.dev')

print(swapi_res)

# pm = swapi.get_film(4)
# jj = swapi.get_person(36)
# for c in pm.get_characters().iter():
#     if c.name == jj.name:
#         print("Why George, why.")
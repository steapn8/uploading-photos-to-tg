import requests
from pathlib import Path
import os


def download_image(filepath, url, api_key = ''):
    payload = {
    "api_key": api_key,
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    
    with open(filepath, 'wb') as file:
        file.write(response.content)
    


def fetch_spacex_last_launch(response):
    response_inside_links = response.json()["links"]
    response_inside_flickr= response_inside_links["flickr"]
    response_inside_original = response_inside_flickr["original"]
    for number, url_spacex in enumerate(response_inside_original):
        resulting_extension = get_extension(url_spacex)
        filename = f'spacex_{number}{resulting_extension}'
        filepath = f"images/{filename}"
        download_image(filepath, url_spacex)

def get_extension(url):
   file_extension = os.path.splitext(url)[1]
   return file_extension

Path("images").mkdir(parents=True, exist_ok=True)


filename = 'hubble.jpeg'
filepath = f"images/{filename}"
# url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
url = ' https://api.nasa.gov/EPIC/api/natural/images'
api_key = 'SUekdgaodoIi9TsVh4tTqPKvUmVTWJ5r5DtO3bK4'
payload = {
    "api_key": api_key,
    # "count":"30"
}

response = requests.get(url, params=payload)
response.raise_for_status()
# plenty_images_day = response.json()
# for number, url_NASA in enumerate(plenty_images_day):
#     resulting_extension = get_extension(url_NASA["url"])
#     print(url_NASA)
#     filename = f'NASA_{number}{resulting_extension}'
#     filepath = f"images/{filename}"
#     download_image(filepath, url_NASA["url"])
    # oh.append(images_day["url"])

# for number, url_spacex in enumerate():
#         resulting_extension = get_extension(url_spacex)
#         filename = f'spacex_{number}{resulting_extension}'
#         filepath = f"images/{filename}"
#         download_image(filepath, url_spacex)
# print(plenty_images_day["hdurl"])url_NASA
image_EPIC = response.json()
# link = response.json()["hdurl"]
for number, fug in enumerate(image_EPIC):
    
    image_EPIC_date_and_seconds = fug["date"].split()
    image_EPIC_date = image_EPIC_date_and_seconds[0].split('-')
    url_EPIC = f"https://api.nasa.gov/EPIC/archive/natural/{image_EPIC_date[0]}/{image_EPIC_date[1]}/{image_EPIC_date[2]}/png/{fug['image']}.png"
    filename = f'EPIC_{number}.png'
    filepath = f"images/{filename}"
    download_image(filepath, url_EPIC, api_key)
# resulting_extension = get_extension(link)
# filename = f'hubble{resulting_extension}'
# filepath = f"images/{filename}"
# print(resulting_extension)
#fetch_spacex_last_launch(response)
# download_image(filepath, link)
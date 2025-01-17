import requests
from downloading_image import download_image, get_extension


filename = 'hubble.jpeg'
filepath = f"images/{filename}"
url = ' https://api.nasa.gov/planetary/apod'
api_key = 'SUekdgaodoIi9TsVh4tTqPKvUmVTWJ5r5DtO3bK4'
payload = {
    "api_key": api_key,
    "count":"30"
}

response = requests.get(url, params=payload)
response.raise_for_status()
plenty_images_day = response.json()
for number, url_NASA in enumerate(plenty_images_day):
    resulting_extension = get_extension(url_NASA["url"])
    print(url_NASA)
    filename = f'NASA_{number}{resulting_extension}'
    filepath = f"images/{filename}"
    download_image(filepath, url_NASA["url"])
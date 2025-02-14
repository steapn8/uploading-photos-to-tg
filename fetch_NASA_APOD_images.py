import requests
from downloading_image import download_image, get_extension
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    url = ' https://api.nasa.gov/planetary/apod'
    api_key = os.getenv('API_KEY_NASA')
    payload = {
        "api_key": api_key,
        "count":"30"  #количество картинок дня
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()
    plenty_day_images = response.json()
    for number, url_nasa in enumerate(plenty_day_images):
        resulting_extension = get_extension(url_nasa["url"])
        filename = f'NASA_{number}{resulting_extension}'
        filepath = f"images/{filename}"
        download_image(filepath, url_nasa["url"])


if __name__ == '__main__':
    main()


import requests
from downloading_image import download_image
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    url = ' https://api.nasa.gov/EPIC/api/natural/images'
    api_key = os.getenv('API_KEY')
    payload = {
        "api_key": api_key,
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()
    image_EPIC = response.json()
    for number, fug in enumerate(image_EPIC):
        
        image_EPIC_date_and_seconds = fug["date"].split()
        image_EPIC_date = image_EPIC_date_and_seconds[0].split('-')
        url_EPIC = f"https://api.nasa.gov/EPIC/archive/natural/{image_EPIC_date[0]}/{image_EPIC_date[1]}/{image_EPIC_date[2]}/png/{fug['image']}.png"
        filename = f'EPIC_{number}.png'
        filepath = f"images/{filename}"
        download_image(filepath, url_EPIC, api_key)


if __name__ == '__main__':
    main()

import requests
from downloading_image import download_image
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    url = ' https://api.nasa.gov/EPIC/api/natural/images'
    api_key = os.getenv('API_KEY_NASA')
    payload = {
        "api_key": api_key,
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()
    image_epic = response.json()
    for number, fug in enumerate(image_epic):
        
        image_epic_date_and_seconds = fug["date"].split()
        image_epic_date = image_epic_date_and_seconds[0].split('-')
        url_epic = f"https://api.nasa.gov/EPIC/archive/natural/{image_epic_date[0]}/{image_epic_date[1]}/{image_epic_date[2]}/png/{fug['image']}.png"
        filename = f'EPIC_{number}.png'
        filepath = f"images/{filename}"
        download_image(filepath, url_epic, api_key)


if __name__ == '__main__':
    main()

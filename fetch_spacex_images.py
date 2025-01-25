from pathlib import Path
from downloading_image import download_image, get_extension
import requests
    
url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
response = requests.get(url)
response.raise_for_status()

def fetch_spacex_last_launch(response):
    response_inside_links = response.json()["links"]
    response_inside_flickr= response_inside_links["flickr"]
    response_inside_original = response_inside_flickr["original"]
    for number, url_spacex in enumerate(response_inside_original):
        resulting_extension = get_extension(url_spacex)
        filename = f'spacex_{number}{resulting_extension}'
        filepath = f"images/{filename}"
        download_image(filepath, url_spacex)
        
fetch_spacex_last_launch(response)
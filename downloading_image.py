import requests
from pathlib import Path
import os


def download_image(filepath, url, api_key = ''):
    Path("images").mkdir(parents=True, exist_ok=True)
    payload = {
        "api_key": api_key,
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    
    with open(filepath, 'wb') as file:
        file.write(response.content)
    


def get_extension(url):
   file_extension = os.path.splitext(url)[1]
   return file_extension




import os
import re
import time

import requests
import jio Saavn_dlp
from lyricsgenius import Genius
from pyrogram.types import CallbackQuery
from jiosaavnsearchpython.__future__ import VideosSearch

from config import Config
from GDNBharath.core.clients import GDNbot
from GDNBharath.core.logger import LOGS
from GDNBharath.helpers.strings import TEXTS


import requests
from bs4 import BeautifulSoup

# URL of the JioSaavn page you want to scrape
url = 'https://www.jiosaavn.com/'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Example: Find the title of the page
    title = soup.find('title').text
    print(f"Page Title: {title}")
    
    # Example: Find all song titles on the page (this will depend on the actual HTML structure of the page)
    songs = soup.find_all('div', class_='song-name')
    for song in songs:
        print(f"Song: {song.text}")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

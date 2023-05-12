import src.config as config
import requests
from bs4 import BeautifulSoup
import random

def find_image(message):
    url = config.YANDEX_URL + message.text
    links = []
    count = 0
    while len(links) == 0 and count < config.COUNT_LINKS:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        links = soup.find_all("img", class_="serp-item__thumb justifier__thumb")
        count += 1
    if count < config.COUNT_LINKS:
        link = random.choice(links).get("src")
        url_photo = "https:" + str(link)
        return url_photo
    else:
        return config.NOT_FOUND


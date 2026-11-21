import requests
from bs4 import BeautifulSoup


def get_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string


# Mengambil judul halaman dari example.com
url = 'https://example.com'
title = get_title(url)
print(f'Judul Halaman: {title}')

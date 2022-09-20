import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

r = requests.get(URL)

soup = BeautifulSoup(r.text, 'html.parser')

for i in soup.find_all(name="h3", class_="title")[::-1]:

    try:
        with open("file.txt", mode="a") as file:

            file.write(f"{i.get_text()}\n")

    except FileNotFoundError:

        with open("file.txt", mode="w") as file:

            file.write(f"{i.get_text()}\n")

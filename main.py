# Importing required libraries
import os
from googletrans import Translator
import requests
from bs4 import BeautifulSoup

# Setting the URL of the web page to be scraped
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Sending an HTTP GET request to the URL and storing the response in a variable r
r = requests.get(URL)

# Parsing the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

# Checking and creating files if they don't exist
for file_name in ["hindi.txt", "english.txt"]:
    if not os.path.exists(file_name):
        with open(file_name, mode="w") as f:
            print(f"{file_name} file created")

# Finding all the movie titles on the page, translating them from English to Hindi, and writing the original and
# translated titles to separate text files
for i in soup.find_all(name="h3", class_="title")[::-1]:
    # Getting the text of the movie title element
    text = i.get_text()

    # Creating a translator object and translating the title from English to Hindi
    translator = Translator()
    translation = translator.translate(text, dest='hi')

    # Writing the original English text to a file named "english.txt"
    with open("english.txt", mode="a") as file:
        file.write(f"{text}\n")

    # Writing the translated Hindi text to a file named "hindi.txt"
    with open("hindi.txt", mode="a") as file:
        file.write(f"{translation.text}\n")

print("Project Done")

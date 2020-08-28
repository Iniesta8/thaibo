#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.yim-yim.de/speisen/mittags-abo/").text

soup = BeautifulSoup(source, "lxml")

print('\n' + soup.h2.text + '\n')

print(soup.strong.text + '\n')

for starter in soup.find_all("p", class_="speisenname"):
    print(starter.text)

print('\n' + "Hauptspeisen:" '\n')

for main_course in soup.find_all("span", class_="speisenname"):
    parent = main_course.find_parent("p")
    print("- " + parent.find(class_="speisenname").text +
          " (" + parent.find(class_="speisenbeschreibung").text.strip() +
          "): " + parent.find(class_="preis").text.strip())


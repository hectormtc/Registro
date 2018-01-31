#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import csv
import shutil
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Firefox()


page = str(input("Write number of page:"))
base_url = "https://en.nametests.com/?page="
url = base_url+str(page)

driver.get(url)

web_requests = requests.get(url)

soup_requests = BeautifulSoup(web_requests.text, 'html.parser')

soup_driver = BeautifulSoup(driver.page_source, 'html.parser')

main = soup_driver.find(class_='hidden-xs')

tags = main.find_all('a')

for tag in tags:
    print("")
    title = tag.text
    print("Title: ", title)
    link = tag.get('href')
    print("Link: ", link)

file_path = 'page_scrap-{page}.csv'.format(page=page)

with open(file_path, "a") as textfile:

    main = soup_driver.find(class_='hidden-xs')
    tags = main.find_all('a')

    for tag in tags:
        print("")
        title = tag.text
        print("Title: ", title)
        link = tag.get('href')
        print("Link: ", link)

        page_line = "{title}\n{link}\n\n".format(
            title=title,
            link=link
        )
        textfile.write(page_line)

file = csv.writer(open(file_path, 'w'))

file.writerow(['Title', 'Link'])
main = soup_driver.find(class_='hidden-xs')
tags = main.find_all('a')

for tag in tags:
    print("")
    title = tag.text
    print("Title: ", title)
    link = tag.get('href')
    print("Link: ", link)
    file.writerow([title, link])
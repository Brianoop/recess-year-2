# Author: Angoda Brian Nyanga
# Date: 26/07/2023
# Github: https://github.com/Brianoop/recess-year-2.git


# WEB-SCRAPPING

# pip3 install beautifulsoup4

# URL to scrape: https://xeno-canto.org/

# import libraries
# from bs4 import BeautifulSoup
# import requests

# url = "https://xeno-canto.org/"
# response = requests.get(url)

# Get title of the page
# soup = BeautifulSoup(response.text, 'html.parser')
# title = soup.find('title')
# print(title)


# Assignment A12: Extract all bird species from the website and generate 
# the csv or JSON file for the bird species, family and more
# Extract all bird songs from the website https://xeno-canto.org/
# Use the following api to get the data: The endpoint for the webservice is at https://xeno-canto.org/api/2/recordings.

# Extract all bird species from the website and generate the csv or JSON file for the bird species family and more

# import libraries
from bs4 import BeautifulSoup
from selenium import webdriver
import time

url_for_all_species = "https://xeno-canto.org/collection/species/all"

"""
INSTRUCTIONS:
1. Use Selenium to load the page dynamically
pip3 install selenium or pip install selenium
2. Install the chrome driver
pip3 install webdriver_manager or pip install webdriver_manager
"""

# Use Selenium to load the page dynamically
driver = webdriver.Chrome()  # Make sure you have the ChromeDriver installed and in the PATH
driver.get(url_for_all_species)
time.sleep(5)  # Wait for the page to load (adjust this value if needed)

# Get title of the page
soup = BeautifulSoup(driver.page_source, 'html.parser')
title = soup.find('title').text
print(title)

# Get all bird species from the table with the class "results"
bird_species = soup.find_all('table', class_='results')
# print(bird_species)
# create list for bird species
bird_species_list = []
for species in bird_species:
    # Find and print all the <td> tags within each <tbody> (bird species)
    td_tags = species.find_all('td')
    for td in td_tags:
        # if td is not a number, print it
        if not td.text.isdigit():
            # get rid of the new line character
            replaced = td.text.replace('\n', '')
            # append to bird_species_list
            bird_species_list.append(replaced)
print(f"Bird species: {bird_species_list}")


# Get all bird species from the table row with the class "extinct"
extinct_missing_bird_species = soup.find_all('tr', class_='extinct')

# create list for extinct 0r missing bird species
extinct_missing_bird_species_list = []

for species in extinct_missing_bird_species:
    # Find and print all the <td> tags within each <tr> (extinct or missing bird species)
    td_tags = species.find_all('td')
    for td in td_tags:
        # if td is not a number, print it
        if not td.text.isdigit():
            # get rid of the new line character
            replaced = td.text.replace('\n', '')
            # append to extinct_missing_bird_species_list
            extinct_missing_bird_species_list.append(replaced)
print(f"Extinct or missing bird species: {extinct_missing_bird_species_list}")


# Close the Selenium WebDriver
driver.quit()


# Using the two lists above, create a csv file
import csv

# create a csv file
with open('bird_species.csv', 'w') as csv_file:
    # create a csv writer object
    csv_writer = csv.writer(csv_file)
    # write the headers
    csv_writer.writerow(['Bird Species', 'Extinct or Missing Bird Species'])
    # write the data
    for i in range(len(bird_species_list)):
        csv_writer.writerow([bird_species_list[i], extinct_missing_bird_species_list[i]])


# Get all bird species family
# bird_species_family = soup.find_all('a', class_='family')
# print(bird_species_family)

# # Get all bird species genus
# bird_species_genus = soup.find_all('a', class_='genus')
# print(bird_species_genus)

# # Get all bird species order
# bird_species_order = soup.find_all('a', class_='order')
# print(bird_species_order)

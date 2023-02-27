import requests
from bs4 import BeautifulSoup
import csv

# Specify the URL to be scraped
url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars'

# Send a request to the website to retrieve the HTML content
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table element containing the star data
table = soup.find('table', {'class': 'wikitable'})

# Find all the rows in the table
rows = table.find_all('tr')

# Open a CSV file for writing
with open('stars.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(['Star name', 'Distance', 'Mass', 'Radius'])

    # Loop through each row in the table
    for row in rows[1:]:
        # Extract the data from the columns
        columns = row.find_all('td')
        star_name = columns[0].text.strip()
        distance = columns[2].text.strip()
        mass = columns[5].text.strip()
        radius = columns[6].text.strip()

        # Write the data to the CSV file
        writer.writerow([star_name, distance, mass, radius])

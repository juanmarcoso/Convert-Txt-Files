import requests
from bs4 import BeautifulSoup
'''
This code will crate a new document .txt converting the input web into a txt file. 
'''
# Specify the URL of the web page you want to convert
url = input("Wich url do you want to convert into a TXT file?: ")

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)
html_content = response.text

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Extract the text from the HTML content
text = soup.get_text()

# Save the text as a new text file
file_name = input("Input the name you want to give to this file: ")
with open(file_name, "w") as file:
    file.write(text)
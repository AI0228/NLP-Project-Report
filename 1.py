from urllib.request import urlopen
from bs4 import BeautifulSoup
import socket

# Set the timeout duration in seconds
timeout_value = 100  # Specify the desired timeout value

# Set the URL to fetch
myurl = "https://www.foxnews.com/sports/patrick-mahomes-fiery-message-win-bills-they-got-what-they-asked-for"

# Open the URL with a timeout
try:
    html = urlopen(myurl, timeout=timeout_value).read()
    soupified = BeautifulSoup(html, "html.parser")
    try_text = soupified.get_text()
    print(try_text)  # Print the first 100 characters of the text
except socket.timeout:
    print("Timeout error: The request took too long to complete.")
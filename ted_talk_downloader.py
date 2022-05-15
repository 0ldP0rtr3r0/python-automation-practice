import requests # getting content of the TED Talk page
import re # regular expression pattern matching
import sys # for argument parsing

# from urllib.request import urlretrieve # downloading MP4
from bs4 import BeautifulSoup # web scraping

# Exception Handling
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter the TED Talk URL")

# url = " "
# url = " "

r = requests.get(url)

print("Download about to start")

soup = BeautifulSoup(r.content, features="lxml")



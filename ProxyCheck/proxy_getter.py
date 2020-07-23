import requests
from bs4 import BeautifulSoup
req = requests.get("https://www.proxynova.com/proxy-server-list/")
response = req.text 
soup = BeautifulSoup(response, 'html.parser')
for link in soup.find_all("tr"):
    print(link)

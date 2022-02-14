from bs4 import BeautifulSoup 
import requests
import dryscrape

uRL = "https://www.realitymod.com/prspy/prbf2/17c498c4f8ba9879c9f13084bfe725133f6a77b1"
session = dryscrape.Session()
session.visit(uRL)
response = session.body()



Html_Content_of_page = requests.get(uRL).text
soup = BeautifulSoup(response)
#soup = BeautifulSoup(Html_Content_of_page, "lxml")

for mapname in soup.find_all('div'):
    print(mapname.text)





import requests 
from bs4 import BeautifulSoup

city = "Santa Rosa"
  
# url and requests 
url = "https://www.google.com/search?q=" + "weather" + city 
html = requests.get(url).content 
  
# getting raw data 
soup = BeautifulSoup(html, 'html.parser') 
temperature = soup.find('div', 
                        attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text 
time_sky = soup.find('div',  
                     attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text 
  
# formatting data 
sky = time_sky.split('\n')[1]

print(sky + " at " + temperature)
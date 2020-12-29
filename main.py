import requests
from bs4 import BeautifulSoup
from plyer import notification
import time
import os

res = requests.get('https://www.worldometers.info/coronavirus/country/turkey/').text
soup = BeautifulSoup(res,'html.parser')
soup.encode('utf-8')
vakalar = soup.find("div", {"class": "maincounter-number"}).get_text().strip()
olumler = soup.find("div", {"class": "maincounter-number"}).get_text().strip()



def VakaBilgilendir(title,message):
    notification.notify(
        title = title,
        message = message,
        app_name='Türkiye Korona',
        timeout = 5)

while True:
    VakaBilgilendir('Türkiye\'de Toplam Vaka Sayısı', vakalar)
    time.sleep(3600) ### Saatlik tekrar.
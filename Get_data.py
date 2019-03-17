import requests
from bs4 import BeautifulSoup

def get_keys():
    URL = 'http://realsungs.dothome.co.kr'
    req = requests.get(URL)
    soup = BeautifulSoup(req.text,'html.parser')
    return soup.p.string
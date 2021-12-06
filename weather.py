from bs4 import BeautifulSoup
import requests

url = 'https://yandex.kz/'
response = requests.get(url)
bs = BeautifulSoup(response.text, 'lxml')

temp = bs.find('div', class_='weather__temp')

print(temp.text)
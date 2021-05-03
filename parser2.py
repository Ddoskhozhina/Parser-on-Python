import requests
from bs4 import BeautifulSoup

def parse():
    URL = 'https://www.olx.kz/elektronika/noutbuki-i-aksesuary/astana/q-%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA/'
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', 'accept': '*/*'
    }
    response = requests.get(URL, headers = HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('div', class_ = 'offer-wrapper')
    
    comps = []
    for item in items:
        comps.append({
            'title': item.find('a', class_ = 'marginright5 link linkWithHash detailsLink linkWithHashPromoted').get_text(strip=True),
            'price': item.find('p', class_ = 'price').get_text(strip=True),
            'link': item.find('a', class_ = 'marginright5 link linkWithHash detailsLink linkWithHashPromoted').get('href')
        })

        global comp
        for comp in comps:
            print(f'{comp["title"]} -> Price: {comp["price"]} -> Link: {comp["link"]}')
            save()

def save():
    with open('parse_info.txt', 'a') as file:
        file.write(f'{comp["title"]} -> Price: {comp["price"]} -> Link: {comp["link"]}\n')

parse()
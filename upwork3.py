from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.youtube.com/user/jacksfilms/videos')

for _ in range(10):
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(3)


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
videos = soup.find_all('div',{'id':'dismissable'})

master_list = []
for video in videos:
    data_dict = {}
    data_dict['title'] = video.find('a',{'id':'video-title'}).text
    data_dict['video_url'] = 'https://www.youtube.com/' + video.find('a',{'id':'video-title'})['href']
    meta = video.find('div',{'id':'metadata-line'}).find_all('span')
    data_dict['views'] = meta[0].text
    data_dict['video_age'] = meta[1].text

    master_list.append(data_dict)

df = pd.DataFrame(master_list)

def convert_views(df):
    if 'K' in df['views']:
        views = float(df['views'].split('K')[0])*1000
        return views
    elif 'M' in df['views']:
        views = float(df['views'].split('M')[0])*1000000
        return views

df['Clean Views'] = df.apply(convert_views, axis=1)
df['Clean Views'] = df['Clean Views'].astype(int)

df.to_csv('output_youtube.csv', index=False)



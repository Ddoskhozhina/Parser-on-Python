import requests
from bs4 import BeautifulSoup
import pandas as pd
from requests.api import get


def get_clinic_name(clinic_id):
    url = 'https://{clinic_id}.portal.athenahealth.com/'
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    clinic_name = soup.find_all('h1')[-1].text.strip()
    return clinic_name

start = 12690
end = 1710
master_list = []

for clinic_id in range(start, end+1):
    data_dict = {}
    data_dict['clinic_id'] = clinic_id
    data_dict['clinic_id'] = get_clinic_name(clinic_id)
    master_list.append(data_dict)
    print(clinic_id)

df = pd.DataFrame(master_list)
df.to_csv('clinic_data.csv', index=False)

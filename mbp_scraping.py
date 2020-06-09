import smtplib
import requests
from bs4 import BeautifulSoup as bp

vanpeople_URL = 'https://www.vanpeople.com/c/s_macbook%20pro/4/0/0/0/0/0.html'
vansky_URL = 'https://www.vansky.com/info/DNSJ01.html?page=1&location=&year=&title=Macbook+Pro'

"""Vanpeople Part"""

vanpeople_page = requests.get(vanpeople_URL)

soup = bp(vanpeople_page.content, 'html.parser')

vanpeople_macbook_title_list = []
vanpeople_macbook_date_list = []
hyper_link_list = []


date_bp = soup.find_all('div', class_='f-fl time')
title_link_bp = soup.find_all('a', href=True, class_='ahtitle')



for i in range(10):
	temp = title_link_bp[i]
	temp2 = date_bp[i]
	vanpeople_macbook_title_list.append(temp.text.strip())
	hyper_link_list.append(temp['href'])
	vanpeople_macbook_date_list.append(temp2.text.strip())

vanpeople_result = zip(vanpeople_macbook_title_list, vanpeople_macbook_date_list, hyper_link_list)

for i in vanpeople_result:
	print(i)

print("-------------------------")
"""Vansky Part"""
hyper_link_prefix = 'https://www.vansky.com/info/'
vansky_page = requests.get(vansky_URL)
soup2 = bp(vansky_page.content, 'html.parser')

vansky_macbook_title_list = []
vansky_macbook_date_list = []
hyper_link_list_vansky = []

title_link_bp = soup2.find_all('a', href=True, class_='adsTitleFont')
date_bp = soup2.find_all('div', class_='adsContentFont visible-xs')

for i in range(10):
	title_link_temp = title_link_bp[i]
	date_temp = date_bp[i]
	vansky_macbook_title_list.append(title_link_temp.text.strip())
	hyper_link_list_vansky.append(hyper_link_prefix + title_link_temp['href'])
	vansky_macbook_date_list.append(date_temp.text.strip())

vansky_result = zip(vansky_macbook_title_list, vansky_macbook_date_list, hyper_link_list_vansky)

for i in vansky_result:
	print(i)


# Send email to myself
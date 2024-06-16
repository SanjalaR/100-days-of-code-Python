import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

FORM = 'https://docs.google.com/forms/d/e/1FAIpQLSfnMu4JHzTcs1b-QmZwbw4DoaJphYSDqha9wh8RQ4rYDCbRBw/viewform?usp=sf_link'
ZILLOW = 'https://appbrewery.github.io/Zillow-Clone/'

response = requests.get(ZILLOW)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())
all_links = soup.select('.StyledPropertyCardDataWrapper a')
links = [link['href'] for link in all_links]
print(links)

all_prices = soup.select('.PropertyCardWrapper__StyledPriceLine')
prices = [price.text.replace('/mo', '').split('+')[0] for price in all_prices]
print(prices)

all_add = soup.select('.StyledPropertyCardDataWrapper address')
add = [a.text.strip() for a in all_add]
print(add)

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.get(FORM)
time.sleep(5)

for i in range(len(links)):
    text_box = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    text_box.send_keys(add[i], Keys.TAB, prices[i], Keys.TAB, links[i], Keys.TAB, Keys.ENTER)
    next_button = driver.find_element(By.LINK_TEXT, value='Submit another response')
    next_button.click()






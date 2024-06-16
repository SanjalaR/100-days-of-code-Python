from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Keep Chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com")

# amazon_url = 'https://www.amazon.in/2022-Apple-MacBook-Laptop-chip/dp/B0B3BMKMGP/ref=sr_1_2?dib=eyJ2IjoiMSJ9.HvIbKicK-wBXX5On3-PhnSsXU75fq8Y4zSe_afkYWsI3Pjv5MAF4OWvZBZoJenxB-cKwWCVvzzdrjSvC-AuDSugHlOUNXElI-xZSNf5yT_1lPE3591oZTf8SaQ_cIyZrOWeeuDSOEx_24wdwTPC7AREEIHjcMnKsoksNvNLw06fEnGsq44B0567Gdb54cVhV.JAycreqzoIdsJNl7pUj_U9KUpMBI2izLiA8bOeg8IvE&dib_tag=se&qid=1717478647&refinements=p_89%3AApple&rnid=3837712031&s=computers&sr=1-2'
# driver.get(amazon_url)
# price = driver.find_element(By.CLASS_NAME, value='a-price-whole')
# print(f'The price is {price.text}')

# driver.get('https://www.python.org')
# search_bar = driver.find_element(By.NAME, value='q')
# print(search_bar.tag_name)
# button = driver.find_element(By.ID, value='submit')
# print(button.size)
# anchor_tag = driver.find_element(By.CSS_SELECTOR, value='.documentation-widget a')
# print(anchor_tag.text)
# submit = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(submit.text)

# elements = [el.text for el in driver.find_elements(By.CSS_SELECTOR, value='.event-widget li')]
# print(elements)
# outer_dict = {}
# i = 0
# for el in elements:
#     things = el.split('\n')
#     inner_dict = {'time': things[0], 'name': things[1]}
#     outer_dict[i] = inner_dict
#     i += 1
# print(outer_dict)

# Clicking on links
# driver.get('https://en.wikipedia.org/wiki/Main_Page')
# count = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
# print(count.text)
# count.click()
# portals = driver.find_element(By.LINK_TEXT, value='Content portals')
# portals.click()

# Sending Keyboard input
# search_bar = driver.find_element(By.NAME, value='search')
# search_bar.send_keys("Python", Keys.ENTER)

# Challenge
# driver.get('https://secure-retreat-92358.herokuapp.com/')
# FIRST_NAME = 'Sanjala'
# LAST_NAME = 'R'
# EMAIL = 'sanhuehdiuwh@hnkidhn.com'
# fname = driver.find_element(By.NAME, value='fName')
# fname.send_keys(FIRST_NAME, Keys.TAB, LAST_NAME, Keys.TAB, EMAIL, Keys.TAB, Keys.ENTER)

# Cookie Clicker
driver.get('http://orteil.dashnet.org/experiments/cookie/ ')
cookie = driver.find_element(By.ID, value='cookie')
items = driver.find_elements(By.CSS_SELECTOR, value='#store div')
item_ids = [item.get_attribute('id') for item in items]
timeout = time.time() + 5
five_min = time.time() + 60*5
while True:
    cookie.click()
    if time.time()>timeout:
        prices = driver.find_elements(By.CSS_SELECTOR, value='#store b')
        item_prices = []
        for price in prices:
            text = price.text
            if text!="":
                cost = int(text.split('-')[1].replace(',',''))
                item_prices.append(cost)

        upgrades = {}
        for n in range(len(item_prices)):
            upgrades[item_prices[n]] = item_ids[n]

        money = driver.find_element(By.ID, value='money').text
        if ',' in money:
            money = money.replace(',','')
        count = int(money)

        affordable = {}
        for cost,id in upgrades.items():
            if count>cost:
                affordable[cost] = id

        highest = max(affordable)
        print(highest)
        to_purchase = affordable[highest]
        driver.find_element(By.ID, value=to_purchase).click()
        timeout = time.time()+5
    if time.time() > five_min:
        cps = driver.find_element(By.ID, value='cps').text
        print(cps)
        break




# driver.close()  # Closes active tab
# driver.quit()  # Closes browser

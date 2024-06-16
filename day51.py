from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
TWITTER_EMAIL = ''
TWITTER_PW = ''

class InternetSpeedTwitterBot():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        time.sleep(3)
        button = self.driver.find_element(By.CSS_SELECTOR, value='.start-button a')
        cont = self.driver.find_element(By.ID, value='onetrust-accept-btn-handler')
        cont.click()
        button.click()
        print('clicked')
        time.sleep(60)
        print('waiting')
        self.down = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        self.up = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)

    def tweet(self):
        self.driver.get('https://twitter.com/login')
        time.sleep(5)
        box = self.driver.find_element(By.NAME, value='text')
        box.send_keys(TWITTER_EMAIL, Keys.ENTER)
        time.sleep(5)
        pw = self.driver.find_element(By.NAME, value='password')
        pw.send_keys(TWITTER_PW, Keys.ENTER)
        time.sleep(5)
        my_tweet = f'Why is my internet speed {self.down}/{self.up} @InternetServiceProvider'
        twitter_box = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        twitter_box.send_keys(my_tweet)

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet()
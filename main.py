import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.chrome.service import Service

USERNAME = "avinashkesarwani007"
PASSWORD = "Imlooser12@"
chrome_driver_path = "C:\Development\chromedriver.exe"


class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)


    def login(self):
        self.driver.get("https://www.instagram.com/")
        self.driver.maximize_window()
        time.sleep(5)

        username = self.driver.find_element_by_name("username")
        username.send_keys("avinashkesarwani007")

        password = self.driver.find_element_by_name("password")
        password.send_keys("Imlooser12@")

        login = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
        login.click()

    def find_followers(self):
        time.sleep(6)
        self.driver.get("https://www.instagram.com/sonali_swami/")

        time.sleep(5)
        followers = self.driver.find_element_by_css_selector("._aa_5 a")
        followers.click()
        time.sleep(3)

        time.sleep(2)
        scrollable_popup = self.driver.find_elements_by_xpath('/html/body/div[6]/div/div/div/div[2]')
        for i in range(50):
            time.sleep(3)
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_popup)
            time.sleep(2)

    def follow(self):
        time.sleep(5)
        followers = self.driver.find_elements_by_css_selector('li button')
        for follower in followers:
            if follower.text == 'Follow':
                follower.click()




bot = InstaFollower(chrome_driver_path)
bot.login()
bot.find_followers()
bot.follow()


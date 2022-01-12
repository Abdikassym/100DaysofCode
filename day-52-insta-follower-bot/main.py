import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Users/77472/Desktop/web development/chromedriver.exe"

USERNAME = "YOUR_USERNAME"
PASSWORD = "YOUR_PASSWORD"
url = "https://www.instagram.com/"


class InstagramBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.get(url=url)
        time.sleep(3)

    def login(self):
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys(USERNAME)

        pass_input = self.driver.find_element_by_name("password")
        pass_input.send_keys(PASSWORD)
        pass_input.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(3)
        search = self.driver.find_element_by_xpath('''//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input''')
        search.send_keys('''python.learning''')
        time.sleep(3)
        search.send_keys(Keys.ENTER)
        search.send_keys(Keys.ENTER)
        time.sleep(3)

        followers = self.driver.find_element_by_xpath('''//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a''')
        followers.click()

    def follow(self):
        time.sleep(3)
        follow_buttons = self.driver.find_elements_by_css_selector("li div button")
        for i in follow_buttons:
            time.sleep(1)
            print(i.click())


bot = InstagramBot()
bot.login()
bot.find_followers()
bot.follow()

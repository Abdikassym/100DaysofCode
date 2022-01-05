import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = "C:/Users/77472/Desktop/web development/chromedriver.exe"

url_twitter = "https://twitter.com/i/flow/login"
url_speed_test = "https://www.speedtest.net/"

username = "default_pixu"
number = "+77472600188"
password = "enderman007"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        # Open website
        self.driver.get(url_speed_test)
        # Click "GO"
        go_btn = self.driver.find_element_by_class_name("start-text")
        go_btn.click()
        time.sleep(60)
        # Gather speed data
        all_data = self.driver.find_elements_by_class_name("result-data-large")
        self.down = float(all_data[1].text)
        self.up = float(all_data[2].text)
        print(f"Download: {self.down}\nUpload: {self.up}")

    def tweet_at_provider(self):
        twit_text = f"""Мой код: 
        Открывается ссылка, с счетчиком скорости интернета, скорость сохраняется.
        Если моя скорость ниже скорости, обещанной Казактелеком, то пишется твит с жалобой и сравнением.
        Скорость на момент твита:
        Скачивание: {self.down} Загрузка: {self.up}"""

        # Launch Twitter Login form
        self.driver.get(url_twitter)
        time.sleep(30)
        print("First step")

        # Log in
        username_input = self.driver.find_element_by_css_selector("label input")
        username_input.send_keys(username)
        username_input.send_keys(Keys.ENTER)
        time.sleep(10)

        # Enter number
        try:
            number_input = self.driver.find_element_by_css_selector("label input")
            number_input.send_keys(number)
            number_input.send_keys(Keys.ENTER)
        except NoSuchElementException:
            pass
        time.sleep(10)

        # Enter password
        pass_input = self.driver.find_element_by_xpath('''//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input''')
        pass_input.send_keys(password)
        pass_input.send_keys(Keys.ENTER)
        time.sleep(15)

        # Click tweet btn
        twit_btn = self.driver.find_element_by_xpath('''//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div''')
        twit_btn.click()
        time.sleep(30)

        # Fill the text
        text_area = self.driver.find_element_by_xpath('''//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div''')
        text_area.click()
        text_area.send_keys(twit_text)
        time.sleep(10)

        # Post twit
        btn = self.driver.find_element_by_xpath('''//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span''')
        btn.click()

twitter_bot = InternetSpeedTwitterBot()
twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider()


import time

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

headers = {
    "Accept-Language": 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}

krisha_url = "https://krisha.kz/prodazha/kvartiry/almaty-almalinskij/?das[_sys.hasphoto]=1&das[live.rooms]=2"
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdVj97R-YRu3LiIlZXc793NO61dVOuWCE3MDM-S5bl8RZP-rw/viewform?usp=sf_link"

response = requests.get(url=krisha_url, headers=headers)
webpage = response.content
soup = BeautifulSoup(webpage, "html.parser")

all_links = [f'https://krisha.kz{link.get("href")}' for link in soup.find_all(class_="a-card__image")]
all_addresses = [address.getText().strip() for address in soup.find_all(class_="a-card__subtitle")]

all_price_elements = [price.getText() for price in soup.find_all(class_="a-card__price")]
all_prices = []
for price in all_price_elements:
    full_price = ""
    for letter in price:
        if letter in numbers:
            full_price += letter
    all_prices.append(full_price)

chrome_driver_path = "C:/Users/77472/Desktop/web development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url=form_url)

for i in range(len(all_addresses)):
    time.sleep(1)
    address = driver.find_element_by_xpath('''//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input''')
    address.send_keys(all_addresses[i])
    price = driver.find_element_by_xpath('''//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input''')
    price.send_keys(all_prices[i])
    link = driver.find_element_by_xpath('''//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input''')
    link.send_keys(all_links[i])
    btn = driver.find_element_by_xpath('''//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span''')
    btn.click()
    time.sleep(1)
    next_btn = driver.find_element_by_xpath('''/html/body/div[1]/div[2]/div[1]/div/div[4]/a''')
    next_btn.click()
    
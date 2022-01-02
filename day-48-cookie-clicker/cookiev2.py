import time
import pprint

from selenium import webdriver

chrome_driver_path = "C:/Users/77472/Desktop/web development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(url)

START_TIME = time.time()
FINISH = START_TIME + 60 * 5
TIMEOUT = 5

cookie = driver.find_element_by_id("cookie")


while START_TIME < FINISH:
    cookie.click()
    START_TIME = time.time()
    shop = {}
    store = [i for i in driver.find_elements_by_css_selector("#store b")]
    del store[-1]
    store.reverse()

    for item in store:
        text_price = item.text.split(" - ")[1]
        price = ""
        for i in text_price:
            if i == ",":
                pass
            else:
                price += i
        price = int(price)
        shop[f"""buy{item.text.split(" - ")[0]}"""] = price

    for name, price in shop.items():
        cookie_count = driver.find_element_by_xpath('//*[@id="money"]').text
        if int(cookie_count) >= price:
            driver.find_element_by_id("name").click()
        else:
            pass

driver.quit()

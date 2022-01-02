import time

from selenium import webdriver

chrome_driver_path = "C:/Users/77472/Desktop/web development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(url)

START_TIME = time.time()
TIMEOUT = START_TIME + 60 * 5
CHECK_SHOP_TIME = 5

cookie = driver.find_element_by_id("cookie")

store = {}


def update_shop():
    shop = driver.find_elements_by_css_selector("#store div b")[::-1][1:]
    for i in range(len(shop)):
        name = "buy" + shop[i].text.split(" - ")[0]
        price = shop[i].text.split(" - ")[1]
        print(name, price)
        store[name] = price


def buy_item():
    global START_TIME
    current_time = time.time()
    if int(current_time) - int(START_TIME) == 5:
        update_shop()
        START_TIME = current_time
        for item in store:
            shop_price = store[item].split(",")
            shop_price = int("".join(shop_price))
            if cookie_count >= shop_price:
                driver.find_element_by_id(item).click()
    else:
        pass
    


while time.time() < TIMEOUT:
    cookie.click()
    cookie_count = int(driver.find_element_by_id("money").text)
    buy_item()

print(driver.find_element_by_id("cps").text)

driver.quit()

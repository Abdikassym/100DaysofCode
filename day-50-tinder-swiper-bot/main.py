from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Users/77472/Desktop/web development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = "https://tinder.com/app/recs"
driver.get(url)
sleep(5)

email = "a*************************m"
password = "e******************************4"

# Log in
log_in_btn = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span")
log_in_btn.click()
sleep(2)

# Click log in with Facebook
facebook_btn = driver.find_element_by_xpath('''/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]''')
facebook_btn.click()
sleep(3)

# Facebook login pop-up
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

# Log in in Facebook
email_input = driver.find_element_by_name("email")
email_input.send_keys(email)

pass_input = driver.find_element_by_name("pass")
pass_input.send_keys(password)
pass_input.send_keys(Keys.ENTER)
sleep(5)

# Agreement page
# continue_btn = driver.find_element_by_xpath('''/html/body/div[1]/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div/div[1]/div/span''')
# continue_btn.click()

# Start in Tinder
driver.switch_to.window(base_window)
print(driver.title)
sleep(10)
# Allow location
allow_location_btn = driver.find_element_by_xpath('''/html/body/div[2]/div/div/div/div/div[3]/button[1]/span''')
allow_location_btn.click()
sleep(1)

# Dismiss notifications
notifications_btn = driver.find_element_by_xpath('''/html/body/div[2]/div/div/div/div/div[3]/button[2]/span''')
notifications_btn.click()

# Accept cookies
cookies_acc_btn = driver.find_element_by_xpath('''/html/body/div[1]/div/div[2]/div/div/div[1]/button/span''')
cookies_acc_btn.click()
sleep(5)

# Swiping right
actions = ActionChains(driver)
i = 0
while True:
    i += 1
    actions.send_keys(Keys.ARROW_LEFT)
    actions.perform()
    print(f"{i} swipe")
    sleep(3)


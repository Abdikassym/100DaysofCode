from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "http://secure-retreat-92358.herokuapp.com/"
chrome_driver_path = "C:/Users/77472/Desktop/web development/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url=url)

f_name = driver.find_element_by_name("fName")
f_name.send_keys("Abdikassym")

l_name = driver.find_element_by_name("lName")
l_name.send_keys("Tolybaev")

email = driver.find_element_by_name("email")
email.send_keys("abdikasymt@gmail.com")
email.send_keys(Keys.ENTER)



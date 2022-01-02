from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://en.wikipedia.org/wiki/Main_Page"
chrome_driver_path = "C:/Users/77472/Desktop/web development/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url=url)

# article_count = driver.find_element_by_css_selector("#articlecount a")
# article_count.click()       # Clicking on a particular element

# technology = driver.find_element_by_link_text("Technology")
# technology.click()      # Clicking on a particular element with a link

search = driver.find_element_by_xpath("""//*[@id="searchInput"]""")
search.send_keys("Python")     # Sends the string that has been stated, not keyboard
search.send_keys(Keys.ENTER)

# driver.quit()

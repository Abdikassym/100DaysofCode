from selenium import webdriver

chrome_driver_path = "C:/Users/77472/Desktop/web development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
python_org = "https://www.python.org/"
driver.get(url=python_org)

# amazon_good = "https://www.amazon.com/Luby-GT606-Pressure-Cooker-340320340mm/dp/B07DWHSPCF/ref=sr_1_1_sspa?crid=2BHNMPH0H8HQQ&keywords=pressure+cooker&qid=1640673886&sprefix=pressure+cooker%2Caps%2C245&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyS0RWVVFUWUNGSllHJmVuY3J5cHRlZElkPUEwODg1NzU4MTU0RDk3ME1IOVBMWSZlbmNyeXB0ZWRBZElkPUEwNTA0NzMwUFRTNDRZWDhXUEJUJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
# price = driver.find_element_by_id("price_inside_buybox")
# print(price.text[1:])

# search_bar = driver.find_element_by_name("q")       # finding particular element by a specific search
# print(search_bar.get_attribute("class"))
#
# logo = driver.find_element_by_class_name("python-logo")     # getting size of a logo using Selenium
# print(logo.size)        # Output: {'height': 82, 'width': 290}. Не ну это пздц как ахуенно

# documentation_link = driver.find_element_by_css_selector(".documentation-widget a").text
# print(documentation_link)     # finding element using a sequence of css selectors

bug_link = driver.find_element_by_xpath("""//*[@id="site-map"]/div[2]/div/ul/li[3]""")
print(bug_link.text)      # Finding particular element using a x-path


# driver.close()      # Closes tab
driver.quit()       # Closes an entire browser



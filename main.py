from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

chrome_driver_path = "C:/Users/77472/Desktop/web development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
driver.get(url)

PHONE_NUMBER = "87472600188"
email = "thespasrabota@gmail.com"
password = "enderman007"
# Login



# 1. Click sign in.
sign_in_btn = driver.find_element_by_xpath('/html/body/div[1]/header/nav/div/a[2]')
sign_in_btn.click()

# 2. Fill the form
login_form = driver.find_element_by_xpath('//*[@id="username"]')
login_form.send_keys(email)

pass_form = driver.find_element_by_xpath('//*[@id="password"]')
pass_form.send_keys(password)
pass_form.send_keys(Keys.ENTER)

# # Start
jobs = []
for i in range(1, 26):
    jobs.append(driver.find_element_by_xpath(f"/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[{i}]/div/div/div[1]/div[2]/div[1]"))

print(len(jobs))

# # 1. Click on "Apply now"
#
# apply_now = driver.find_element_by_css_selector(".jobs-apply-button--top-card button")
# apply_now.click()
#
# # 2. Entering phone number
# phone_number_input = driver.find_element_by_xpath('//*[@id="urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2858285727,41053098,phoneNumber~nationalNumber)"]')
# phone_number_input.send_keys(f"{PHONE_NUMBER}")
#
# # 3. Clicking next
# first_next_btn = driver.find_element_by_xpath('''/html/body/div[3]/div/div/div[2]/div/form/footer/div[2]/button''')
# first_next_btn.click()
#
# # 4. Click next again.
# second_next_btn = driver.find_element_by_xpath('''/html/body/div[3]/div/div/div[2]/div/form/footer/div[2]/button[2]''')
# second_next_btn.click()
#
# # 5. Answering questions
# questions = driver.find_elements_by_css_selector(".jobs-easy-apply-form-section__grouping input")
#
# for i in questions:
#     i.send_keys("123")
#
# # 6. Click next.
# third_next_btn = driver.find_element_by_xpath('''/html/body/div[3]/div/div/div[2]/div/form/footer/div[2]/button[2]''')
# third_next_btn.click()
#
#
# # 7. Send application
# send_btn = driver.find_element_by_xpath('''/html/body/div[3]/div/div/div[2]/div/div[2]/footer/div[3]/button[2]''')
# send_btn.click()
#
# sleep(3)
#

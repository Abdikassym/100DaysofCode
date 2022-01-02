from selenium import webdriver

driver = webdriver.Chrome(executable_path=chrome_driver_path)
python_org = "https://www.python.org/"
driver.get(url=python_org)

events = {}

calendar = [eve.text for eve in driver.find_elements_by_css_selector(".event-widget .shrubbery li")]
for i in range(len(calendar)):
    time = calendar[i].split('\n')[0]
    name = calendar[i].split('\n')[1]
    events[i] = {
        "time": time,
        "name": name
    }

print(events)
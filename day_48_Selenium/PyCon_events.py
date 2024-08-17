from selenium import webdriver
from selenium.webdriver.common import by
by = by.By()
driver = webdriver.Firefox()
driver.get(url='https://www.python.org/')

event_dates = driver.find_elements(by.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(by.CSS_SELECTOR, ".event-widget li a")

events = {}

for n in range(len(event_dates)):
    events[n] = {
        "time": event_dates[n].text,
        "name": event_names[n].text

    }

print(events)

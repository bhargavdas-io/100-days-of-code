from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
by = by.By()
driver = webdriver.Firefox()
driver.get(url="http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(by.NAME, value="fName")
lname = driver.find_element(by.NAME, value="lName")
email = driver.find_element(by.NAME, value="email")
fname.send_keys("Bhargav")
lname.send_keys("Das")
email.send_keys("bhargavdas15@gmail.com", Keys.ENTER)


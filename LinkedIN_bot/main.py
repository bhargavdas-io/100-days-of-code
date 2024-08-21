import os
import time
from selenium import webdriver
from selenium.webdriver.common import keys
from dotenv import load_dotenv
from selenium.webdriver.common.by import By

load_dotenv()
LINKED_IN = "https://www.linkedin.com/checkpoint/lg/sign-in-another-account"
ID = os.environ["LOGIN_ID"]
PASS = os.environ["PASSWRD"]
JOB_LINK = os.environ["JOB_LINK"]


driver = webdriver.Firefox()
keys = keys.Keys()
driver.get(url=LINKED_IN)

username = driver.find_element(By.NAME, value="session_key")
password = driver.find_element(By.NAME, value="session_password")
button = driver.find_element(By.XPATH, value="/html/body/div/main/div[2]/div[1]/form/div[3]/button")

username.send_keys(ID)
password.send_keys(PASS)
time.sleep(2)
button.click()

time.sleep(2)

driver.get(url=JOB_LINK)








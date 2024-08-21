import os
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from time import sleep
from dotenv import load_dotenv

load_dotenv()
PHN = os.environ["PHN"]
keys = keys.Keys()
options = FirefoxOptions()
options.set_preference("geo.prompt.testing", True)
options.set_preference("geo.prompt.testing.allow", True)
driver = webdriver.Firefox(options=options)
driver.get(url='https://tinder.com/')
sleep(4)

login_button = driver.find_element(By.CSS_SELECTOR, value="[href='https://tinder.onelink.me/9K8a/3d4abb81']")
sleep(4)
login_button.click()

sleep(4)
cookies = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div[2]/div/div/div[1]/div[1]/button')
cookies.click()

try:
    phone_login = driver.find_element(By.XPATH,
                                      '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[3]/button')
    sleep(2)
    phone_login.click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="phone_number"]').send_keys(PHN)
    sleep(2)
    next_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div/div[3]/button')
    next_button.click()
    sleep(2)
except NoSuchElementException:
    more_options = driver.find_element(By.XPATH,
                                       value="/html/body/div[2]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/button")
    more_options.click()
    phone_num = driver.find_element(By.XPATH,
                                    value="/html/body/div[2]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[3]/button")
    phone_num.click()
    driver.find_element(By.XPATH, value='//*[@id="phone_number"]').send_keys(PHN)
    sleep(2)
    next_b = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[1]/div/div[3]/button')
    next_b.click()
sleep(10)
captcha = input("Press enter after solving captcha and entering OTP, if any.")
print("Click Next and press enter....")
sleep(2)
print("Click on Send mail.")
mail_otp = input("Press enter after providing the e-mail OTP")
sleep(2)

location_button = driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div/div/div[3]/button[1]")
location_button.click()
sleep(10)

notification_button = driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div/div/div[3]/button[2]")
notification_button.click()
sleep(25)
for n in range(100):
    sleep(5)
    print("Auto Liking...")
    like = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button')
    like.click()
print("Liked 100 Tinder Profiles!")


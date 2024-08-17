from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.amazon.in/dp/B00949CTQQ?ref=nb_sb_ss_w_as-reorder_k0_1_7&amp=&crid=32SDOD5WXS8VU&amp=&sprefix=paulas+")
price = driver.find_element(By.CLASS_NAME,"a-price-whole").text
print(price)




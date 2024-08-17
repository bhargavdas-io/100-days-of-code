import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import smtplib
from dotenv import load_dotenv
load_dotenv()
SEND = os.environ["EMAIL"]
PASS = os.environ["PASSWORD"]
RECEIVER = os.environ["RECEIVER"]


driver = webdriver.Firefox()
driver.get("https://www.amazon.in/dp/B00949CTQQ?ref=nb_sb_ss_w_as-reorder_k0_1_7&amp=&crid=32SDOD5WXS8VU&amp=&sprefix=paulas+")
price = driver.find_element(By.CLASS_NAME,"a-price-whole").text
print(price)
lowest_price = "2,295"

if price <= lowest_price:
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=SEND, password=PASS)
        connection.sendmail(from_addr=SEND, to_addrs=RECEIVER,
                            msg=f"Paula's Choice EXFOLIATE is at all time low @ Rs.{price}")
else:
    print("Price is at the inflated rate.")


from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException,TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def testSetup():
    assert testSetup() == "setup"
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-popup")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe", options=options)
    time.sleep(3)
    url = "https://www.yad2.co.il/realestate/rent/flats?page="
    page = 2
    current_url = url + str(page)
    driver.get(current_url)
    time.sleep(5)
    print("Passed")
    driver.close()



def testIterator():
    assert testIterator() == "iterator"

    options = webdriver.ChromeOptions()
    options.add_argument("--disable-popup")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe", options=options)
    time.sleep(3)
    url = "https://www.yad2.co.il/realestate/rent/flats?page="
    page = 2
    current_url = url + str(page)
    driver.get(current_url)
    time.sleep(5)
    print("Passed")

    for i in range(4):
        a = driver.find_element_by_id('feed_item_{}'.format(i))
        a.location_once_scrolled_into_view
        a.click()
        time.sleep(1)
        print(i)

        phone_number = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "phone_number_{}".format(i))))

        contact_seller = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "contact_seller_{}".format(i))))

        if phone_number.is_displayed():
            phone_number.click()

        elif contact_seller.is_displayed():
            contact_seller.click()

            time.sleep(1)
    print("Passed")
    driver.quit()







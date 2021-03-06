from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException,TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

#Fixture for Chrome







#Fixture for Chrome
@pytest.fixture(scope="class")
def chrome_driver_init(request):
    driver = webdriver.Chrome(executable_path="/usr/bin/google-chrome")
    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.usefixtures("chrome_driver_init")
class BasicTest:
    driver = webdriver.Chrome(executable_path="/usr/bin/google-chrome")
    driver.get("https://www.yad2.co.il/realestate/rent/flats?page=2")
    time.sleep(5)
    for i in range(40):
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


class TestURL(BasicTest):
        def test_open_url(self):
            self.driver.get("https://www.yad2.co.il/")
            print(self.driver.title)
            self.driver.quit()
            print("next page passed")













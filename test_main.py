from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException,TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

#Fixture for Chrome
@pytest.fixture(scope="class")
def chrome_driver_init(request):
    chrome_driver = webdriver.Chrome()
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()

@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass
class Test_URL(BasicTest):
        def test_open_url(self):
            self.driver.get("https://www.yad2.co.il/")
            print(self.driver.title)

            sleep(5)

@pytest.mark.usefixtures("chrome_driver_init")
class Basic_Chrome_Test:
    pass
class Test_URL_Chrome(Basic_Chrome_Test):
        def test_open_url(self):
            self.driver.get("https://www.yad2.co.il")
            print(self.driver.title)
            sleep(5)



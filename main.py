import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


#good browsers
#Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
#Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36


class RealOptions:
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=C:\\Users\\swagabit\\AppData\\Local\\Google\\Chrome\\User Data")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path="C:\webdriver\‏‏chromedriver_2.exe", options=options)



class FakeOptions:
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=C:\\Users\\swagabit\\AppData\\Local\\Google\\Chrome\\")
    options.add_argument("--disable-popup")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path="C:\webdriver\‏‏chromedriver_1.exe", options=options)



class Initiate(FakeOptions,RealOptions):
    def __init__(self):

        time.sleep(3)
        url = "https://www.yad2.co.il/realestate/rent/flats?page="
        page = 2
        current_url = url+str(page)
        FakeOptions.driver.get(current_url)
        time.sleep(5)

        information = []

        def iterator():

            def product_locator():
                while True:
                    try:
                        for i in range(41):
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
                                information.append(phone_number)

                        i+=1

                    except ElementClickInterceptedException:
                        pass
                    except NoSuchElementException:
                        return
                    except TimeoutException:
                        return


            product_locator()
            current_url = FakeOptions.driver.current_url

            #yad2 doesnt support IE
            if "internet-explorer" in FakeOptions.driver.current_url:
                print("[ERROR] IE is not supported. Restarting...")
                FakeOptions.driver.quit()
                FakeOptions
                time.sleep(3)
                return

            #first captcha
            if "validate" in FakeOptions.driver.current_url:
                print("Run!!! captcha quitting...")
                FakeOptions.driver.quit()
                time.sleep(3)

                RealOptions.driver = webdriver.Chrome(executable_path="C:\webdriver\‏‏chromedriver_2.exe", options=RealOptions.options)
                time.sleep(5)
                RealOptions.driver.get(url + str(page))
                product_locator()

                if "validate" in RealOptions.driver.current_url:
                    print("Run!!! captcha second time...")
                    RealOptions.driver.quit()
                    time.sleep(3)

                    CopiedOptions.driver = webdriver.Chrome(executable_path="C:\webdriver\‏‏chromedriver_3.exe",options=RealOptions.options)
                    time.sleep(5)
                    driver.get(url + str(page))
                    product_locator()

        def nextPage(url,page,driver):
            driver.get(url + str(page))
            time.sleep(2)

        while True:

            page+=1
            iterator()

            #closing after each 5 pages
            print("scrapped:",driver.current_url)
            if page % 5 == 0:
                print("Scrapped 5 pages, restarting for better performance...")
                driver.quit()
                driver = webdriver.Chrome(executable_path="C:\webdriver\‏‏chromedriver_5.exe", options=FakeOptions.options)

            nextPage(url,page,driver)


if __name__ == '__main__':
    Initiate()




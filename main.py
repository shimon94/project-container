import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#Seperated class to change options and profiles while script is runing.
#Use it for random user agents, and ip rotation best for projects that need multiple browsers in the same session.
class MyOptions:
    options = webdriver.ChromeOptions()
    
class Initiate(MyOptions):
    def __init__(self):
        driver = webdriver.Chrome('your path', options=MyOptions.options)
        time.sleep(3)
        url = "https://www.yad2.co.il/realestate/rent/flats?page="
        page = 2
        current_url = url+str(page)
        driver.get(current_url)
        time.sleep(5)
        def iterator():
            def product_locator():
                #iterates between 40 listings each page
                while True:
                    try:
                        for i in range(41):
                            a = driver.find_element_by_id('feed_item_{}'.format(i))
                            a.location_once_scrolled_into_view
                            a.click()
                            time.sleep(1)
                            print(i)
                            #id may be either of the options below.
                            phone_number = WebDriverWait(driver, 10).until(
                                EC.presence_of_element_located((By.ID, "phone_number_{}".format(i))))

                            contact_seller = WebDriverWait(driver, 10).until(
                                EC.presence_of_element_located((By.ID, "contact_seller_{}".format(i))))
                                    
                            if phone_number.is_displayed():
                                phone_number.click()

                            elif contact_seller.is_displayed():
                                contact_seller.click()

                                time.sleep(1)

                        i+=1

                    except ElementClickInterceptedException:
                        pass
                    except NoSuchElementException, TimeoutException:
                        return

            product_locator()
            current_url = driver.current_url

            #site doesnt support IE
            if "internet-explorer" in driver.current_url:
                print("[ERROR] IE is not supported. Restarting...")
                driver.quit()

                
            #first captcha
            if "validate" in driver.current_url:
                print("Run!!! captcha quitting... (Demo mode, no handling with captcha for more help you may contact me.")
                driver.quit()
                time.sleep(3)
                
        def nextPage(url,page,driver):
            driver.get(url + str(page))
            time.sleep(2)

        while True:
            page+=1
            iterator()
            #closing after each 5 pages 
            if page % 5 == 0:
                print("Scrapped 5 pages, restarting for better performance...")
                driver.quit()
                driver = webdriver.Chrome('your path', options=MyOptions.options)
                 
            nextPage(url,page,driver)


if __name__ == '__main__':
    Initiate()




import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
time.sleep(1)
search_box = driver.find_element_by_name("q")
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(2)
driver.quit()

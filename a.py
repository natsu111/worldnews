from selenium import webdriver
import urllib.request
from bs4 import BeautifulSoup
import time
import lxml

driver = webdriver.Chrome()
driver.get('https://www3.nhk.or.jp/nhkworld/zh/news/')
time.sleep(1)

for i in range(1, 5):
    val = "//*[@id='p-top']/div/div/div[2]/div[1]/div[%d]/div[1]/div[1]/a" % i
    time.sleep(1)
    driver.find_element_by_xpath(val).click()
    title = driver.find_elements_by_xpath(
        '//*[@id="p-article"]/div[1]/h1/span')
    body = driver.find_elements_by_xpath('//*[@id="p-article"]/div[3]')
    for j in title:
        print(j.text)

    for j in body:
        print(j.text)
    time.sleep(1)
    driver.back()


driver.quit()
# time.sleep(1)
# driver.quit()

# for i in range(1, 5):
#     a = "hellonumber%dsan" % i
#     print(a)

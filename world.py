from selenium import webdriver
import urllib.request
from bs4 import BeautifulSoup
import time
import lxml

driver = webdriver.Chrome()
url = 'https://www3.nhk.or.jp/nhkworld/zh/news/'
driver.get(url)
time.sleep(1)
driver.find_element_by_xpath(
    '//*[@id="p-top"]/div/div/div[1]/div/div[2]/div[1]/a').click()

title = driver.find_elements_by_xpath('//*[@id="p-article"]/div[1]/h1/span')
body = driver.find_elements_by_xpath('//*[@id="p-article"]/div[3]')

for i in title:
    print(i.text)

for i in body:
    print(i.text)

time.sleep(1)
driver.back()

for i in range(1, 9):
    val = "//*[@id='p-top']/div/div/div[2]/div[1]/div[%d]/div[1]/div[1]/a" % i
    if len(driver.find_elements_by_xpath(val)) > 0:
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
    else:
        break


driver.quit()

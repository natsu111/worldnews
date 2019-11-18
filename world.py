from selenium import webdriver
import urllib.request
from bs4 import BeautifulSoup
import time
import lxml

path = './a.csv'
driver = webdriver.Chrome()
url = 'https://www3.nhk.or.jp/nhkworld/zh/news/'
driver.get(url)
time.sleep(1)
driver.find_element_by_xpath(
    '//*[@id="p-top"]/div/div/div[1]/div/div[2]/div[1]/a').click()

title = driver.find_elements_by_xpath('//*[@id="p-article"]/div[1]/h1/span')
body = driver.find_elements_by_xpath('//*[@id="p-article"]/div[3]')

with open(path, mode='a') as f:
    f.write('*******************************************************\n\n')

for i in title:
    with open(path, mode='a') as f:
        f.write(i.text + '\n')

for i in body:
    with open(path, mode='a') as f:
        f.write(i.text + '\n\n')

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
            with open(path, mode='a') as f:
                f.write(j.text + '\n')

        for j in body:
            with open(path, mode='a') as f:
                f.write(j.text + '\n\n')
        time.sleep(1)
        driver.back()
    else:
        break
with open(path, mode='a') as f:
    f.write('*******************************************************\n\n')

driver.quit()

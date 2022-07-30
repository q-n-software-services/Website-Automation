import time
import pyautogui as pt
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
os.environ['PATH'] += r"C:/Users/HP/PycharmProjects/pythonProject5/chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_extension('extension_1_6_7_0.crx')
time.sleep(5)
driver = webdriver.Chrome(options=options)
#chrome.get("https://w2.leisurelink.lcsd.gov.hk/leisurelink/index/index.jsp?lang=en")

# driver = webdriver.Chrome()
driver.get("https://w2.leisurelink.lcsd.gov.hk/leisurelink/index/index.jsp?lang=en")

'''first_element = driver.find_element_by_id('iamsmartLogin')
first_element.click()
driver.implicitly_wait(30)
time.sleep(30)'''

my_element = driver.find_element_by_id('LCSD_2')
my_element.click()
driver.implicitly_wait(30)
time.sleep(15)

positions1 = pt.locateCenterOnScreen('continue.png', grayscale=False, confidence=0.9)
print(positions1)
print()
print()
pt.moveTo(positions1)
pt.click()

positions2 = pt.locateAllOnScreen('continue.png', grayscale=False, confidence=0.9)
for i in positions2:
    print(i)
    print(i[0], i[1], i[2], i[3])

'''element_2 = driver.find_element(By.CLASS_NAME, 'actionBtnBlock')
element_2.click()
driver.implicitly_wait(30)
time.sleep(15)

element_3 = driver.find_element(By.CLASS_NAME, 'actionBtnBlock')
element_3.click()
driver.implicitly_wait(30)
time.sleep(15)

import datetime
import time

now = datetime.datetime.now()
print(now.hour, now.minute, now.second)

element_4 = driver.find_element()
element_4.click()
driver.implicitly_wait(30)'''


'''time.sleep(30)
cookies = [{'domain': '.t2.leisurelink.lcsd.gov.hk', 'httpOnly': True, 'name': 'TS01415b60', 'path': '/', 'secure': False, 'value': '01f2d17a0f50aa67f1ce21f182769482aef541d49050a293525b7d1d4884776503db5d7239a600081b955e740e3cc4ff0128b368d8'}, {'domain': 't2.leisurelink.lcsd.gov.hk', 'httpOnly': True, 'name': 'BIGipServereweb_transaction_443', 'path': '/', 'secure': True, 'value': '1427548352.47873.0000'}, {'domain': '.t2.leisurelink.lcsd.gov.hk', 'expiry': 3233125250, 'httpOnly': False, 'name': 'l8VhPa4e', 'path': '/', 'secure': False, 'value': 'Axl8PGaBAQAAok4aDST1bUZA7-3Lvm1uZ41gz5eaxZoIYRo-AIUfAMeVX-9hAS04xWSuckQBwH8AAEB3AAAAAA|1|0|395adf1ca61cd0bdf6aa582d8fac3f75b0c4c47a'}, {'domain': 't2.leisurelink.lcsd.gov.hk', 'httpOnly': True, 'name': 'JSESSIONID', 'path': '/', 'secure': True, 'value': 'Q2ZmPHkFc7hEh9ZW8gOmlpCPzYNq4h1JSdvQxtGlE6_myzljn7XF!-256464978!786161446'}]
cookies = [{'domain': 't2.leisurelink.lcsd.gov.hk', 'httpOnly': True, 'name': 'TS01415b60', 'path': '/', 'secure': False, 'value': '01f2d17a0f50aa67f1ce21f182769482aef541d49050a293525b7d1d4884776503db5d7239a600081b955e740e3cc4ff0128b368d8'}, {'domain': 't2.leisurelink.lcsd.gov.hk', 'httpOnly': True, 'name': 'BIGipServereweb_transaction_443', 'path': '/', 'secure': True, 'value': '1427548352.47873.0000'}, {'domain': 't2.leisurelink.lcsd.gov.hk', 'expiry': 3233125250, 'httpOnly': False, 'name': 'l8VhPa4e', 'path': '/', 'secure': False, 'value': 'Axl8PGaBAQAAok4aDST1bUZA7-3Lvm1uZ41gz5eaxZoIYRo-AIUfAMeVX-9hAS04xWSuckQBwH8AAEB3AAAAAA|1|0|395adf1ca61cd0bdf6aa582d8fac3f75b0c4c47a'}, {'domain': 't2.leisurelink.lcsd.gov.hk', 'httpOnly': True, 'name': 'JSESSIONID', 'path': '/', 'secure': True, 'value': 'Q2ZmPHkFc7hEh9ZW8gOmlpCPzYNq4h1JSdvQxtGlE6_myzljn7XF!-256464978!786161446'}]
cookies = [{'domain': 'https://w2.leisurelink.lcsd.gov.hk/leisurelink/index/index.jsp?lang=en', 'httpOnly': True, 'name': 'TS01415b60', 'path': '/', 'secure': False, 'value': '01f2d17a0f50aa67f1ce21f182769482aef541d49050a293525b7d1d4884776503db5d7239a600081b955e740e3cc4ff0128b368d8'}, {'domain': 'https://w2.leisurelink.lcsd.gov.hk/leisurelink/index/index.jsp?lang=en', 'httpOnly': True, 'name': 'BIGipServereweb_transaction_443', 'path': '/', 'secure': True, 'value': '1427548352.47873.0000'}, {'domain': 'https://w2.leisurelink.lcsd.gov.hk/leisurelink/index/index.jsp?lang=en', 'expiry': 3233125250, 'httpOnly': False, 'name': 'l8VhPa4e', 'path': '/', 'secure': False, 'value': 'Axl8PGaBAQAAok4aDST1bUZA7-3Lvm1uZ41gz5eaxZoIYRo-AIUfAMeVX-9hAS04xWSuckQBwH8AAEB3AAAAAA|1|0|395adf1ca61cd0bdf6aa582d8fac3f75b0c4c47a'}, {'domain': 'thttps://w2.leisurelink.lcsd.gov.hk/leisurelink/index/index.jsp?lang=en', 'httpOnly': True, 'name': 'JSESSIONID', 'path': '/', 'secure': True, 'value': 'Q2ZmPHkFc7hEh9ZW8gOmlpCPzYNq4h1JSdvQxtGlE6_myzljn7XF!-256464978!786161446'}]

for i in cookies:
    driver.add_cookie(i)
driver.implicitly_wait(30)
driver.refresh()'''
# driver.get('https://t2.leisurelink.lcsd.gov.hk/lcsd/leisurelink/dispatchFlow.do?lang=EN&osName=Windows&winId=be60859f-9b11-677d-59a1-96d790eeab7b&tokenLifetime=600')
# my_c = driver.get_cookies()
# print(my_c)

'''driver = [0, 0, 0,0, 0]
for i in range(5):
    driver[i] = webdriver.Chrome()
    driver[i].get("https://w2.leisurelink.lcsd.gov.hk/leisurelink/index/index.jsp?lang=en")
    driver[i].implicitly_wait(30)
    my_element = driver[i].find_element_by_id('LCSD_2')
    my_element.click()
'''
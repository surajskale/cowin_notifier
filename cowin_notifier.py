from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from playsound import playsound


chrome_browser = webdriver.Chrome(executable_path="D:\chromedriver")

chrome_browser.get('https://www.cowin.gov.in/home')

chrome_browser.maximize_window()

pin = 413507

while True:
    chrome_browser.refresh()

    chrome_browser.find_element_by_xpath(
        '/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div[1]/input').send_keys(pin)

    chrome_browser.find_element_by_xpath(
        '/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div[1]/div/button').click()

    time.sleep(10)

    na = chrome_browser.find_elements_by_class_name('no-available')
    print(len(na))
    if(len(na) != 29):
        playsound('E:\\PythonProjects\\StockMarketTrading\\Ironman.mp3')

    time.sleep(60)
# list = chrome_browser.find_element_by_xpath("/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[6]/div/div/div/div/div/div/div[2]/ul")

# for child in list.find_elements_by_xpath(".//*"):
#     print(child)

# print(list)

# res = chrome_browser.find_element_by_xpath('/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[6]/div/div/div/div/div/div/div[2]/ul/li[4]')

# print(res)

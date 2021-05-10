from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from playsound import playsound


chrome_browser = webdriver.Chrome(executable_path="D:\chromedriver")

chrome_browser.get('https://www.cowin.gov.in/home')

chrome_browser.maximize_window()

#Enter pin-code for your respective area instead of 99999 below.
pin = 99999

while True:
    chrome_browser.refresh()

    chrome_browser.find_element_by_xpath(
        '/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div[1]/input').send_keys(pin)

    chrome_browser.find_element_by_xpath(
        '/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div[1]/div/button').click()

    # you can change sleep timer based on your internet connection.
    
    time.sleep(10)

    not_available = chrome_browser.find_elements_by_class_name('no-available')
    print(len(not-available))
    if(len(not-available) != 29):
        # you have to enter the mp3 file location which is played when slots are available.
        playsound('E:\\PythonProjects\\Cowin\\Ironman.mp3')
        
    # you can change sleep timer based on your internet connection.
    time.sleep(60)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome = webdriver.Chrome()#使用程控瀏覽器
chrome.get("https://www.gmail.com")#至該網站
time.sleep(0.5)
inputBar = chrome.find_element_by_tag_name("inputWrapper")
inputBar.send_keys("player333617@gmail.com")
time.sleep(0.5)
inputBar.send_keys(Keys.ENTER)

"""
time.sleep(0.5)
chrome.find_element_by_partial_link_text("猿創力程式設計學校-")
time.sleep(0.5)
chrome.maximize_window()
time.sleep(0.5)
chrome.get_screenshot_as_file("猿創力.png")
time.sleep(0.5)
"""
chrome.close()

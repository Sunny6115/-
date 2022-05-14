from selenium import webdriver
from bs4 import BeautifulSoup
import time
chrome = webdriver.Chrome()#使用程控瀏覽器
chrome.get("https://tw.eztable.com/search?country=tw&date=2022-05-11&people=2&searchTab=restaurant&source=mobile.eztable.com")#至該網站
time.sleep(3)

for i in range(7):
    chrome.execute_script('window.scrollTo(0,document.body.scrollHeight);')#將拉調往下拉
    time.sleep(1)
    
soup = BeautifulSoup(chrome.page_source,"html.parser")
for div in soup.find_all('div',class_ ="row sc-drKuOJ cJLQnl"):
    Name = div.find("h4")
    productName = Name.text
    Price = div.find('span',class_ ="sc-cugefK gFcUdK")
    productPrice = Price.text
    print('餐廳:'+productName+'價格:'+productPrice)
chrome.close()
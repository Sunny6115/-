import requests#呼叫requests函式庫
from bs4 import BeautifulSoup#在bs4裡呼叫BeautifulSoup函式庫
import re#呼叫re函式庫
'''
創造一個名為respond的變數並將從網址裡得到的html存入
創造一個名為soup的變數並用BeautifulSoup過濾出respond內的文字存入
創造一個名為a_tags的變數並在soup裡找出a的資料存入
'''
respond = requests.get("https://www.books.com.tw/web/sys_saletopb/books/") 
soup = BeautifulSoup(respond.text,"html.parser")

a_tags = soup.find_all('a')
'''
不知道
如果從url內從第一行開始往後過濾與排行榜相同的網址並存入url裡'href'的list的動作回傳的數值不等於=None執行以下命令
印出url的文字加上:url['href']內的網址
'''
for url in a_tags:
    if re.fullmatch("https://www.books.com.tw/web/sys_saletopb/books/(\d+)/[?]loc=P_0002_(\d+)",url['href']) != None:
        print(url.text+':'+url['href'])
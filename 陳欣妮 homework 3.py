import requests
from bs4 import BeautifulSoup
res = requests.get('https://www.books.com.tw/web/sys_saletopb/books')
soup = BeautifulSoup(res.text,'html.parser')
lis = soup.find_all("li",class_="item")


amount = 0
for index,each_li in enumerate(lis):
    bookName = ""
    img = each_li.find("img")
    imgSrc = img['src']
    imgRespond = requests.get(imgSrc)
    
    h4 = each_li.find('h4')
    if not h4:
        continue
    a = h4.find('a')
    if not a:
        continue
    bookname = str(index+1)+'-'+ a.text

    
    ul = each_li.find('ul')
    li = ul.find('li')
    strong = li.find('a')
    if strong:
        bookname = bookname+'-'+strong.text

    with open(bookname+".jpg","bw") as file:
        file.write(imgRespond.content)
    
    
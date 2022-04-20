import re#呼叫re函式庫

string = input("請輸入gmail:")#詢問gmail並將收到的字串存入變數
print(re.match("\w+@gmail.com",string))#辨識變數裡的字串是否符合gmail的規格，是的話就印出來
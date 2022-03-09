# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 20:50:10 2022

@author: USER
"""
import requests

url = "https://gaeabooks.pixnet.net/blog"

data = requests.get(url)
print (data)

print(data.text)

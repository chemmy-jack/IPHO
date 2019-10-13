import requests
import os
# from selenium import webdriver
# from bs4 import BeautifulSoup

os.chdir('/Users/ck-kuo/Desktop/temp')

file_list = []
for i in range(2014,2020) :
    file_list.append('http://web.kshs.kh.edu.tw/physics/olympia%20exams/file/%E5%88%9D%E8%A9%A6/'+str(i)+'%E7%89%A9%E7%90%86%E5%A5%A7%E6%9E%97%E5%8C%B9%E4%BA%9E%E5%88%9D%E8%A9%A6-%E9%A1%8C%E7%9B%AE.pdf')
# print(file_list)
x = 2014
for i in file_list :
    print(i)
    local = '/Users/ck-kuo/Desktop/temp/'+ str(x) +'.pdf'
    print(local)
    r = requests.get(i)
    open(local, 'wb').write(r.content)
    x += 1
    print(" finnish ")

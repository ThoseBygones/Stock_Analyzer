# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 00:21:36 2018

@author: 30517
"""

import requests
from bs4 import BeautifulSoup
import re
 
def getHTMLText(url): #爬取股票网站代码
    try:
        r = requests.get(url)
        r.raise_for_status() #测试网址是否正确
        r.encoding = r.apparent_encoding
        return r.text  #返回股票代码
    except:
        return ""
# 构造得到股票编号列表的函数
def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html, 'html.parser')#将html内容形成树状 
    a = soup.find_all('a')#找到所有的a标签（超链接）
    for i in a:
        try:
            href = i.attrs['href']#找出属性对应的内容
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])#找出与herf[0]相匹配的字符串，以列表形式返回；findall查找全部r标识代表后面是正则的语句
        except:
            continue
# 构造得到股票信息的函数 
def getStockInfo(lst, stockURL, fpath):
    count = 0
    for stock in lst:
        url = stockURL + stock + ".html"#得到具体单支股票页面的html
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            # 找到属性为"class":"stock-bets"，名称为div的标签
            stockInfo = soup.find('div',attrs={'class':'stock-bets'})

            # 在div标签中，找到属性为"class":"bets-name"的标签
            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            # update:将一个字典传入另一个字典中；字典添加键值对，其中name.text为name标签中的文本信息，包括换行符和空字符，利用split（）函数后，返回股票名字和标号的列表。
            infoDict.update({'股票名称': name.text.split()[0]})

            # 在div标签中，找到所有dt标签
            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val

            print(str(infoDict))
             
            with open(fpath, 'a', encoding='utf-8') as f:
                f.write( str(infoDict) + '\n' )
                count = count + 1
               
            if count == 10:
                break
            
        except:
            # count = count + 1
            continue



def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'D:/BaiduStockInfo.txt'
    slist=[]
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)
 
main()
# coding = UTF-8
# -*- coding: cp936 -*-
# 爬取李东风PDF文档,网址：http://www.math.pku.edu.cn/teachers/lidf/docs/textrick/index.htm
from bs4 import BeautifulSoup
import urllib.request
import re
import os
from selenium import webdriver

# open the url and read

def getHtml(url):
    browser = webdriver.Chrome

    page = browser.get(url)  # 这个就是chrome浏览器中的element的内容了

  #  browser.find_elements_by_tag_name('a')  # 获取element中 td下的内容

   # page = urllib.request.urlopen(url)
   # page = requests.get(url)
   # html = page.read()


    html = page.text.encode(page.encoding).decode()
    print(html)
    page.close()
    return html

# compile the regular expressions and find
# all stuff we need
def getUrl(html):
    print(1)
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all('a', href=re.compile(r".*pdf$"))


    print(tags)
    print(2)
    return(tags)



def getFile(url):
    file_name = url.split('/')[-1]
    global Max_Num
    Max_Num = 6
    for i in range(Max_Num):
        try:
            u = urllib.request.urlopen(url, timeout=5)
            f = open(file_name, 'wb')

            block_sz = 8192
            while True:
                buffer = u.read(block_sz)
                # print(buffer)
                if not buffer:
                    break

                f.write(buffer)
            f.close()
            print("Sucessful to download" + " " + file_name + " ！")

            break
        except:
            if i < Max_Num - 1:
                continue
            else:
                print
                'URLError: <urlopen error timed out> All times is failed'






#raw_url = 'http://vip.stock.finance.sina.com.cn/corp/view/vCB_BulletinGather.php?ftype=ndbg&page=1'

os.mkdir('pdf_download1')
os.chdir(os.path.join(os.getcwd(), 'pdf_download1'))
for i in range(1, 5):
   begin = i
   print('=========================================================================================================')
   print('Begin the {} time crawl'.format(i))
   print('=========================================================================================================')

   raw_url = 'http://www.sse.com.cn/home/search/?webswd=%E5%AE%A1%E8%AE%A1%20%E5%B1%A5%E8%81%8C%E6%8A%A5%E5%91%8A'
   html = getHtml(raw_url)
   tags = getUrl(html)
   time = 0

   for tag in tags:
      time = 1 + time
      print('The ' + str(begin) + ' time crawl! Crawl the ' + str(time) + ' firm ！')
      print(tag.text)
      print(tag.get('href'))
      url = tag.get('href')
      getFile(tag.text)
      print('---------------------------------------------------------------------------------------------------------')
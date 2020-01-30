# coding = UTF-8
# -*- coding: cp936 -*-
import urllib.request
import time
import re
import os
from selenium import webdriver

def getpdf_link(url):

    path = "/usr/local/bin/chromedriver.exe"  # chromedriver完整路径，path是重点

    driver = webdriver.Chrome(path)
    driver.get(url)
    driver.implicitly_wait(10)
    time.sleep(5)

    pdf_link = []

    for page in range(1, 154):

        page = 1 + page

        print('Crawl the page ' + str(page - 1) + ' firms ！')
        print(
            '---------------------------------------------------------------------------------------------------------')

        for link in driver.find_elements_by_tag_name('a'):

            pdf_link.append({'title': link.get_attribute('title'), 'href': link.get_attribute('href'),
                             'page': page - 1})

        try:
            b = driver.find_element_by_class_name('nextPage')
            b.click()

        except:
            print
            'Page ' + str(page) + ' is the end page !'




    driver.quit()

    return pdf_link



def pdf_fillter(pdf_link):

    pdf_link_fillter = []

    for atag in pdf_link:

        if re.search(r'.*报告', atag['title']):
            pdf_link_fillter.append(atag)

    return pdf_link_fillter


def getpdf_file(pdf_link_fillter):

    for atag in pdf_link_fillter:

        file_name = atag['title'] + '.pdf'

        global Max_Num
        Max_Num = 6
        for i in range(Max_Num):
            try:
                u = urllib.request.urlopen(atag['href'], timeout=10)
                f = open(file_name, 'wb')
                p = atag['page']



                block_sz = 8192

                while True:
                    buffer = u.read(block_sz)
                    if not buffer:
                        break
                    f.write(buffer)
                f.close()
                print("Sucessful to download the firm " + " in pages " + str(p) + " named " + file_name  + " ！")

                break

            except:
                if i < Max_Num - 1:
                    continue
                else:
                    print
                    'URLError: <urlopen error timed out> All times is failed'
















os.mkdir('pdf_download1')
os.chdir(os.path.join(os.getcwd(), 'pdf_download1'))

print('=========================================================================================================')
print('Begin the crawl')
print('=========================================================================================================')

raw_url = 'http://www.sse.com.cn/home/search/?webswd=%E5%AE%A1%E8%AE%A1%E5%A7%94%E5%91%98%E4%BC%9A%20%E5%B1%A5%E8%81%8C%E6%8A%A5%E5%91%8A'  #"http://www.sse.com.cn/home/search/?webswd=%E5%B1%A5%E8%81%8C%E6%8A%A5%E5%91%8A"
pdf_link = getpdf_link(raw_url)
pdf_link_fillter = pdf_fillter(pdf_link)
getpdf_file(pdf_link_fillter)

print('=========================================================================================================')
print('Finish the crawl')
print('=========================================================================================================')








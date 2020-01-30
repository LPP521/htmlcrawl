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

    for page in range(1, 101):

        page = 1 + page

        print('Crawl the page ' + str(page - 1) + ' firms ！')
        print(
            '---------------------------------------------------------------------------------------------------------')

        for index, link in enumerate(driver.find_elements_by_class_name('ahover')):



            #print(str(link.get_attribute('innerHTML')))

            a1 = re.compile(r'(\d{4}-\d{2}-\d{2})$')
            a2 = re.compile(r'(\d{4})')
            a3 = re.compile(r'<span title="" class="r-title">(.*)</em></span>')

            #print(re.findall(a3, str(link.get_attribute('innerHTML'))))
            h1 = re.findall(a1, str(link.get_attribute('href')))
            h11 = ''.join(h1)
            h2 = link.get_attribute('data-id')
            y1 = re.findall(a2, str(link.get_attribute('innerHTML')))
            year = ''.join(y1)
            n1 = re.findall(a3, str(link.get_attribute('innerHTML')))
            name = ''.join(n1)
            name = name.replace('<em>', '')
            name = name.replace('</em>', '')
            #print(name)

            href = 'http://static.cninfo.com.cn/finalpage/' + str(h11) + '/' + str(h2) + '.PDF'
            pdf_link.append({'code': link.get_attribute('data-seccode'), 'year': year, 'name': name, 'href': href,
                             'page': page - 1, 'seconds': index + 1})
            print(pdf_link)





        try:
            b = driver.find_element_by_class_name('btn-next')
            b.click()

        except:
            print
            'Page ' + str(page) + ' is the end page !'

    driver.quit()
    #print(pdf_link)
    return pdf_link


def getpdf_file(pdf_link):

    for atag in pdf_link:

        file_name = atag['code'] + '-' + atag['year'] + '-' + atag['name'] + '.pdf'

        global Max_Num
        Max_Num = 6
        for i in range(Max_Num):
            try:
                u = urllib.request.urlopen(atag['href'], timeout=10)
                f = open(file_name, 'wb')
                p = atag['page']
                s = atag['seconds']



                block_sz = 8192

                while True:
                    buffer = u.read(block_sz)
                    if not buffer:
                        break
                    f.write(buffer)
                f.close()
                print("Sucessful to download the " + str(s) + " firm " + " in pages " + str(p) + " named " + file_name  + " ！")

                break

            except:
                if i < Max_Num - 1:
                    continue
                else:
                    print
                    'URLError: <urlopen error timed out> All times is failed'




os.mkdir('pdf_download3')
os.chdir(os.path.join(os.getcwd(), 'pdf_download3'))

raw_url = ['http://www.cninfo.com.cn/new/fulltextSearch?notautosubmit=&keyWord=2013+%E5%AE%A1%E8%AE%A1%E5%A7%94%E5%91%98%E4%BC%9A%E5%B1%A5%E8%81%8C%E6%8A%A5%E5%91%8A',
           'http://www.cninfo.com.cn/new/fulltextSearch?notautosubmit=&keyWord=2014+%E5%AE%A1%E8%AE%A1%E5%A7%94%E5%91%98%E4%BC%9A%E5%B1%A5%E8%81%8C%E6%8A%A5%E5%91%8A',
           'http://www.cninfo.com.cn/new/fulltextSearch?notautosubmit=&keyWord=2015+%E5%AE%A1%E8%AE%A1%E5%A7%94%E5%91%98%E4%BC%9A%E5%B1%A5%E8%81%8C%E6%8A%A5%E5%91%8A',
           'http://www.cninfo.com.cn/new/fulltextSearch?notautosubmit=&keyWord=2016%E5%AE%A1%E8%AE%A1%E5%A7%94%E5%91%98%E4%BC%9A%E5%B1%A5%E8%81%8C%E6%8A%A5%E5%91%8A',
           'http://www.cninfo.com.cn/new/fulltextSearch?notautosubmit=&keyWord=2017%E5%AE%A1%E8%AE%A1%E5%A7%94%E5%91%98%E4%BC%9A%E5%B1%A5%E8%81%8C%E6%8A%A5%E5%91%8A',
           'http://www.cninfo.com.cn/new/fulltextSearch?notautosubmit=&keyWord=2018%E5%AE%A1%E8%AE%A1%E5%A7%94%E5%91%98%E4%BC%9A%E5%B1%A5%E8%81%8C%E6%8A%A5%E5%91%8A']
            #"http://www.sse.com.cn/home/search/?webswd=%E5%B1%A5%E8%81%8C%E6%8A%A5%E5%91%8A" 13,14,15,16(1088),17(1249),18(1292)

for index, url in enumerate(raw_url):

    print('=========================================================================================================')
    print('Begin the ' + str(2013+index) + ' crawl')
    print('=========================================================================================================')


    pdf_link = getpdf_link(url)
    getpdf_file(pdf_link)

    print('=========================================================================================================')
    print('Finish the ' + str(2013+index) + ' crawl')
    print('=========================================================================================================')






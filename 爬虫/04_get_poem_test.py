#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 14:49
# @Author  : Xuegod Teacher For
# @File    : 04_get_poem_test.py
# @Software: PyCharm
'''
第一步：获取所有古诗的超链接
第二步：从每一首古诗的超链接拿到内容
'''
#http urllib？ requests pip install requests
import requests
#爬虫：模拟浏览器的，主要模拟的是浏览器的版本，pip install fake-useragent
from fake_useragent import UserAgent
#pip install bs4
from bs4 import BeautifulSoup
#线程，进程，协程
from concurrent.futures import ThreadPoolExecutor,wait,ALL_COMPLETED
#全体的url地址
urls = [
    'https://so.gushiwen.org/gushi/tangshi.aspx',
    'https://so.gushiwen.org/gushi/songci.aspx',
    'https://so.gushiwen.org/gushi/sanbai.aspx',
]
#请求头部信息，把脚本伪装成浏览器
headers = {
    'User-Agent':UserAgent().random
}
#todo:获取所有古诗的超链接
def get_all_poem_link(urls):
    poem_links = []
    for url in urls:
        req = requests.get(url,headers=headers)
        #获取响应体
        # print(req.text)
        #美丽汤bs匹配的规则
        soup = BeautifulSoup(req.text,'lxml')
        #下一步请求的内容
        content = soup.find_all('div',class_ = 'sons')[0]
        #在一步拿到a标签
        links = content.find_all('a')
        # print(links)
        for link in links:
            poem_links.append('https://so.gushiwen.org'+link['href'])
    return poem_links

poem_list = []
#todo:从每一首古诗的超链接拿到内容
def get_poem(url):

    req = requests.get(url,headers=headers)
    soup = BeautifulSoup(req.text,'lxml')

    poem = soup.find('div',class_='contson').text.strip()
    # print(poem)

    poem_list.append(poem)
if __name__ == '__main__':
    poem_links = get_all_poem_link(urls)
    #利用线程池并发执行，最大并发量10
    executor = ThreadPoolExecutor(max_workers = 10)
    #利用submit提交每一个线程任务
    future_tasks = [executor.submit(get_poem,url) for url in poem_links]
    #等待所有的线程结束之后我的程序一次往下走
    wait(future_tasks,return_when= ALL_COMPLETED)


    for poem in poem_list:

        print(poem)
        with open('poem.txt','a',encoding='utf-8') as f:
            f.write(poem+'\n')



    # print(poem_links)
    # get_poem('https://so.gushiwen.org/shiwenv_f324eea45183.aspx')


import requests
from lxml import etree
import json

base_url = "http://www.xiachufang.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
}

count = None
contents = None
item = {}
shicai_list = []

def get_link():
    link_list = []
    url = "http://www.xiachufang.com/category/957/?page=%s"
    for i in range(1,12):
        response = requests.get(url=url%i, headers=headers)
        html = etree.HTML(response.text)
        links = html.xpath('//div[@class="ing-recipe"]//div[@class="normal-recipe-list"]//p[@class="name"]/a/@href')
        for i in links:
            link = base_url + i
            link_list.append(link)
    return link_list

def get_info():
    link_list = get_link()
    for link in link_list:
        response2 = requests.get(url=link,headers=headers)
        html = etree.HTML(response2.text)
        title = html.xpath('//h1[@class="page-title"]/text()')[0].strip()
        yongliao = html.xpath('//table//tr')
        img_src = html.xpath('//img[@itemprop="image"]/@src')[0]
        img_response = requests.get(img_src,headers=headers)
        if "|" in title:
            title = title.replace("|","_")
        if "/" in title:
            title = title.replace("/", "_")
        print("正在下载：%s..."%title)
        with open("images/"+title+".jpg","wb") as f:
            f.write(img_response.content)
        for cailiao in yongliao:
            Materials_used = cailiao.xpath('./td[1]/a/text()')
            if not Materials_used:
                pass
            else:
                Materials_used = Materials_used[0]
                count = cailiao.xpath('./td[2]/text()')
                if not count:
                    count = "适量"
                else:
                    count = count[0].strip()
                    global contents
                    contents = cailiao.xpath('//li[@class="container"]/p/text()')
                    shicai_list.append(Materials_used + "    "+count)
        item["菜名"] = title
        item["食材用量"] = shicai_list
        item["步骤"] = contents
        f = open("caipu.json","a",encoding="utf-8")
        f.write(json.dumps(item,ensure_ascii=False,indent=4)+",\n")
        f.close()

if __name__ == '__main__':
    get_info()






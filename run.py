import os
import requests
from lxml import etree
import pymysql
import random
import re
import sys

user_agent = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    "UCWEB7.0.2.37/28/999",
    "NOKIA5700/ UCWEB7.0.2.37/28/999",
    "Openwave/ UCWEB7.0.2.37/28/999",
    "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
    "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",
]

files = os.listdir('.')  # 如果path为None，则使用path = '.' 

for filename in files:
    portion = os.path.splitext(filename)  # 分离文件名与扩展名
    if portion[1] == '.tex':
        newname = filename

file_object = open(newname,'r')


f = open('out.txt','w')#, encoding='UTF-8')
try:
    for line in file_object:
        g = re.search("bibitem{", line)
        if g:
            f.writelines(line)
finally:
     file_object.close()

a = open('result_arxiv.txt','a')
b = open('result_researchgate.txt','a')

def get_info_arxiv(url,origin_title):
    headers = {'User-Agent': random.choice(user_agent)}
    r = requests.get(url,headers=headers,timeout=5)
    r.encoding = r.apparent_encoding
    html = etree.HTML(r.text)
    href = html.xpath('//li[@class="arxiv-result"]//a[1]/@href') #names为list属性  names列表有10个元素，对应每个标题
    title = html.xpath('string(//li[@class="arxiv-result"]//p[@class="title is-5 mathjax"])')  #用于判断检索得到的第一个结果是否是我们要找的，因为有时候即使不匹配，网页也会返回结果
    title = title.strip()
    # print(title)
    # print(origin_title[0])
    if title!=origin_title[0].strip('.'):
        href = []
    if len(href)==0:
        print("Not found in Arxiv\n")
        a.write("Not found in Arxiv\n"+"\n")
    else:
        print("Address:"+href[0]+"\n")
        a.write("Address:"+href[0]+"\n"+"\n")

def find_urls_arxiv(path):
    titles = []
    origin = []
    pattern = re.compile("\"(.*)\"")
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            title = pattern.findall(line)
            if len(title)!=0:
                origin.append(title)
                title[0].replace(",", "%2C").replace(":", "%3A").strip(".")
                s = title[0].split(" ")
                titles.append("+".join(s))
            else:
                print(line+"Invalid title\n")
    for i in range(len(titles)):
        url = "https://arxiv.org/search/?query=" + titles[i] + "&searchtype=all&source=header"
        print(titles[i].replace('+',' '))
        a.write(titles[i].replace('+',' ')+"\n")
        get_info_arxiv(url, origin[i])

def get_info_researchgate(url,origin_title):
    headers = {'User-Agent': random.choice(user_agent)}
    r = requests.get(url,headers=headers,timeout=5)
    # time.sleep(5)
    r.encoding = r.apparent_encoding
    html = etree.HTML(r.text)
    # print(r.text)
    href = html.xpath('//div[@class="nova-o-stack__item"][1]//a[@class="nova-e-link nova-e-link--color-inherit nova-e-link--theme-bare"]/@href') #names为list属性  names列表有10个元素，对应每个标题
    title = html.xpath('string(//div[@class="nova-o-stack__item"][1]//a[@class="nova-e-link nova-e-link--color-inherit nova-e-link--theme-bare"])')  #用于判断检索得到的第一个结果是否是我们要找的，因为有时候即使不匹配，网页也会返回结果
    title = title.strip()
    # print(title.lower())
    # print(origin_title[0].strip(".").lower())
    if title == "Source":
        print("Address:" + "https://www.researchgate.net/" + href[0] + "\n")
        return
    if title.lower()!=origin_title[0].strip('.').lower():
        href = []
    if len(href)==0:
        print("Not found in Researchgate\n")
        b.write("Not found in Researchgate\n"+"\n")
    else:
        print("Address:"+ "https://www.researchgate.net/" +href[0]+"\n")
        b.write("Address:"+ "https://www.researchgate.net/" +href[0]+"\n"+"\n")


def find_urls_researchgate(path):
    titles = []
    origin = []
    pattern = re.compile("\"(.*)\"")
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            title = pattern.findall(line)
            if len(title)!=0:
                origin.append(title)
                title[0].replace(",", "%2C").replace(":", "%3A").strip(".")
                s = title[0].split(" ")
                titles.append("+".join(s))
            else:
                print(line+"Invalid title\n")
    for i in range(len(titles)):
        url = "https://www.researchgate.net/search/publication?&q=" + titles[i]
        #print(url)
        print(titles[i].replace('+',' '))
        b.write(titles[i].replace('+',' ')+"\n")
        get_info_researchgate(url, origin[i])

print("type a to search in Arxiv and type r to search in Researchgate(a/r)")

arg=input();
if arg=='a':
    find_urls_arxiv("out.txt")
elif arg=='r':
    find_urls_researchgate("out.txt")

'''
if sys.argv[1]=='a':
    find_urls_arxiv("out.txt")
elif sys.argv[1]=='r':
    find_urls_researchgate("out.txt")
else :
    print("use a to search in Arxiv and type r to search in Researchgate")
    print(sys.argv)
'''
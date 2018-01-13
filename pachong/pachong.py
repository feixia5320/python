#----------------打开本地的html------------
#解析器：html5lib、html.parser

from bs4 import BeautifulSoup

info = []
with open('/Users/Administrator/Desktop/1_1code_of_video/the_blah.html','r')  as wb_data:
    Soup =BeautifulSoup(wb_data, 'html5lib')
    images = Soup.select('body > div.main-content > ul > li > img')
    titles = Soup.select('body > div.main-content > ul > li > h3 > a')
    descs = Soup.select('body > div.main-content > ul > li > p')
    # print(images,title, desc,sep="\n---------------------\n")

for title,image,desc in zip(titles,images,descs):
    data = {
        "title" : title.get_text(),
        "image" : image.get('src'),
        "desc" : desc.get_text()
    }

    info.append(data)
    print(data)


#--------------打开url---------------------
import requests
from bs4 import BeautifulSoup

url = 'http://www.baidu.com'
req = requests.get(url)
req.encoding = 'utf-8'
soup = BeautifulSoup(req.content, 'html.parser')
print(soup)

#------------------爬取网页---------------
'''
#header中保存了已经登录的用户信息，爬取个人登录的界面
headers = {
    'User-Agent':'',
    'Cookie':''
}
wb_data = requests.get(url,headers=headers)
'''
from bs4 import BeautifulSoup
import requests
import time

url = 'https://cn.tripadvisor.com/Attractions-g60763-Activities-New_York_City_New_York.html'
urls = ['https://cn.tripadvisor.com/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#ATTRACTION_LIST'.format(str(i)) for i in range(30,930,30)]

headers = {
    'User-Agent':'',
    'Cookie':''
}
def get_favs(url,data=None):
    wb_data = requests.get(url,headers=headers)
    soup      = BeautifulSoup(wb_data.text,'html5lib')
    titles    = soup.select('a.location-name')
    imgs      = soup.select('div.photo > div.sizedThumb > img.photo_image')
    metas = soup.select('span.format_address')

    if data == None:
        for title,img,meta in zip(titles,imgs,metas):
            data = {
                'title'  :title.get_text(),
                'img'    :img.get('src'),
                'meta'   :list(meta.stripped_strings)
            }
            print(data)

for single_url in urls:
    get_favs(single_url)

'''
alink    = soup.select('a')
print(alink[0]['href'])
'''
#-----------将爬取的网页输出excel、数据库------------

import pandas
import sqlite3

arr = [
    {
        "aa": "aa",
        "bb": "bb",
        "cc": "cc"
    },{
        "aa": "aa",
        "bb": "bb",
        "cc": "cc"
    }
]
#使用pandas数据分析
df = pandas.DataFrame(arr)
#显示前5条数据
df.head(5)
#输出为excel
# df.to_excel('aaaa.xls')

with sqlite3.connect('news.sqlite') as db:
    #写入数据库
    df.to_sql('news', con=db)
    #读取数据库
    df2 = pandas.read_sql_query('SELECT * FROM news', con=db)
    #输入出为excel
    df2.to_excel('bbbb.xls')

#在数据库中创建表
zufang  = sqlite3.connect('zufang.sqlite')
create_table = 'create table zufang (title varchar(512), money varchar(128))'
zufang.execute(create_table)

#-----------------urllib-post-------------
from urllib import request, parse
url = r'http://www.lagou.com/jobs/positionAjax.json?'
headers = {
    'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
    'Connection': 'keep-alive'
}
data = {
    'first': 'true',
    'pn': 1,
    'kd': 'Python'
}
data = parse.urlencode(data).encode('utf-8')
req = request.Request(url, headers=headers, data=data)
page = request.urlopen(req).read()
page = page.decode('utf-8')

#-----------------urllib-异常处理--------------
def get_page(url):
    headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                    r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
        'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
        'Connection': 'keep-alive'
    }
    data = {
        'first': 'true',
        'pn': 1,
        'kd': 'Python'
    }
    data = parse.urlencode(data).encode('utf-8')
    req = request.Request(url, headers=headers)
    try:
        page = request.urlopen(req, data=data).read()
        page = page.decode('utf-8')
    except error.HTTPError as e:
        print(e.code())
        print(e.read().decode('utf-8'))
    return page

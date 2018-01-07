#打开本地的html
#解析器：html5lib、html.parser

from bs4 import BeautifulSoup

with open('/Users/Administrator/Desktop/1_1code_of_video/the_blah.html','r')  as wb_data:
    Soup =BeautifulSoup(wb_data, 'html5lib')

    for link in Soup.find_all('a'):
        print(link.get('href'))
    print(Soup)
    
#打开url
import requests
from bs4 import BeautifulSoup

url = 'http://www.baidu.com'
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
print(soup)


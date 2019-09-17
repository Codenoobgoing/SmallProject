import requests
from bs4 import BeautifulSoup
import re
import pymysql

db = pymysql.connect(host = '127.0.0.1',port = 3306, db = 'chen', user = 'root',password = 'root',charset = 'utf8')
#创建游标
cursor = db.cursor()
cursor.execute('select * from image')
print(cursor.fetchall())



#驼峰
#获取图片列表
def getImagesList(page):
    #获取斗图源代码
    html = requests.get('https://www.doutula.com/photo/list/?page='+str(page)).text
    #正则表达式 通配符 .*? 非贪婪匹配，匹配所有   分组匹配
    reg = r'data-original="(.*?)".*?alt="(.*?)"'
    pattern = re.compile(reg, re.S)
    imagelist = re.findall(pattern, html)
    for i in imagelist:
        image_url = i[0]
        image_title = i[1]
        cursor.execute("insert into image(`name`,`image`) values('{}','{}')".format(image_title, image_url))
        print('正在保存 %s'%image_title)
        db.commit()

for i in range(1,2778):
    print('第{}页'.format(i))
    getImagesList(i)
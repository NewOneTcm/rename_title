#! python3
# -*- coding: utf-8 -*-
import os
from bs4 import BeautifulSoup

filePath = os.path.join(os.getcwd(),'text') #读取text中路径
fileList = os.listdir(filePath) #读取路径中文件

j=0 #设置新文件的下标为0
newPath = os.getcwd()+'\\'+'new' 
os.mkdir(newPath) #在当前目录下创建new文件夹


for i in  fileList:
    fileTotolPath =''

    html= i
    fileTotolPath = os.path.join(filePath,i) #将文件夹路径与文件名合并
    htmlfile = open(fileTotolPath, 'r', encoding='utf-8') #打开网页文件

    soup = BeautifulSoup(htmlfile, 'html.parser') #解析网页文件

    htmlFileName = "{:0>3d}".format(j+1) + '.html' #设置新文件的规则    
    savePath = os.path.join(newPath,htmlFileName) #设置保存的新路径
    
    soup.title.string.replace_with(i) #关键语句，将title中的文本替换为网页文件名

    with open(savePath, 'w', encoding='utf-8') as f: #保存为新文件
      f.write(str(soup)) #写文件
      print(i + ' work done.')
      j=j+1 #为新文件更新下标
print('all done.')

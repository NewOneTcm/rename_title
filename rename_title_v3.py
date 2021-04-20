#! python3
# modified :2021-4-20
# -*- coding: utf-8 -*-
import os
import logging # 引入logging模块
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s') # logging.basicConfig函数对日志的输出格式及方式做相关配置
# 由于日志基本配置中级别设置为DEBUG，所以一下打印信息将会全部显示在控制台上
from bs4 import BeautifulSoup

import glob

filePath = os.path.join(os.getcwd())
logging.debug('fileList=%s',filePath)

fileList = []

fileList = glob.glob(r'*.html')  ##获得该目录下所有html文件
logging.debug('fileList=%s',fileList)



j=0
newPath = os.getcwd()+'\\'+'new'
if(not os.path.exists(newPath)):
    os.mkdir(newPath)


for i in  fileList:
    
    fileTotolPath =''
    logging.debug('filename=%s',i)
    html= i
    fileTotolPath = os.path.join(filePath,i)
    logging.debug('fileTotolPath=%s',fileTotolPath)
    htmlfile = open(fileTotolPath, 'r', encoding='utf-8')
    logging.debug('type(htmlfile)=%s',type(htmlfile))
    logging.debug('htmlfile=%s',htmlfile)
    soup = BeautifulSoup(htmlfile, 'html.parser')
    logging.debug('soup=%s',soup)
    logging.debug('type(soup)=%s',type(soup))
    logging.debug('soup.title=%s',soup.title.string)
    htmlFileName = "{:0>3d}".format(j+1) + '.html'
    
    savePath = os.path.join(newPath,htmlFileName)

    try:     
        soup.title.string.replace_with(i)
        logging.debug('soup=%s',soup) 

    except Exception as error:
        print(error)
    finally:
        with open(savePath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
            print(i + ' work done.')
        j = j+1
print('all done.')

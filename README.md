# rename_title

# 修改网页的标题为网页文件名的操作

最近一直使用supermemo导入文件，但是导入过程中，发现很多网页的标题名字都是一样，这样就分不清阅读文章的顺序了。批量修改网页的标题为原网页文件名，这样就可以达到目的的。

## 安装BeautifulSoup库文件

安装方法：打开cmd，输入pip install BeautifulSoup，等待安装完成即可。

## 更新版本
使用过程中，发现有些并不是直接使用text文件夹的，所以我修改为，将py文件放在html文件当前目录，同时新建一个new文件夹，并将新建的文件保存在new文件夹中。修改代码见rename_title_v2.py 

2020-3-5 生姜

如果要看代码解释的，看下面的内容

## 替换标题代码：
```python
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
```

将代码保存为rename_title.py。放在epub下的`text`目录同级下。

代码默认使用`text`文件夹的html文件。如果你的不是`text`文件夹，你修改本地的`text`文件夹，或者修改代码上第5行上的text名称，与你当前的文件夹名称保持一致即可。

```
filePath = os.path.join(os.getcwd(),'text') #读取text中路径
```

双击rename_title.py文件即可完成更名过程。




## 导入supermemo

进入new文件夹，可以看到已经改名后的文件。导入SM，按文件名进行排序



2021-01-28 14:03:02

生姜

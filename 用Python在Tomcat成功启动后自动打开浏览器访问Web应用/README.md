# 用Python在Tomcat成功启动后自动打开浏览器访问Web应用 #

creation date:2020-03-20 13: 55: 11

tag:Tomcat

## 前提条件 ##

1. Windows
2. Python 2.7
3. 需设置`CATALINA_HOME`环境变量

## 放码过来 ##

```python
# -*- coding: utf-8 -*
import os
import time
import subprocess

tomcatStartFilePath = 'C:\\tomcat\\apache-tomcat-7.0.90-windows-x64\\apache-tomcat-7.0.90\\bin\\startup.bat'
browserPath = 'C:\\Users\\Administrator.USER-20180302VA\\AppData\\Local\\360Chrome\\Chrome\\Application\\360chrome.exe'
appAddress = "http://localhost:8080/nice"

# 启动 tomcat,注意要设置CATALINA_HOME的环境变量
subprocess.Popen(tomcatStartFilePath, shell=True)
print 'Starting tomcat...'
time.sleep(15)

# 启动15s后, 轮询 8080端口是否启用
print 'Polling...'
startBrowerFalg = False

#每次轮询间隔5秒
interval = 5
count = 6

while count > 0:
    tmpFile = os.popen('netstat -na','r')
    breakWhileFlag = False
    for line in tmpFile.readlines():
        if line.startswith('  TCP    0.0.0.0:8080'):
            breakWhileFlag = True
            break
    print "Not yet."
    if breakWhileFlag:
        print "It's Ok."
        startBrowerFalg = True
        break
    else:
        count -= 1
        time.sleep(interval)

# 8080 启用成功后， 打开浏览器访问 /nice
if startBrowerFalg:
    print "Launch the browser."
    subprocess.Popen('%s %s'%(browserPath, appAddress))
else:
    print "Something wrong ..."
    raw_input()
```

## 参考资料 ##

1. [如何通过批处理调用tomcat的startup.bat，然后在tomcat启动成功后，自动打开浏览器并定位到指定网址](https://zhidao.baidu.com/question/539535706.html)
2. [Python编程快速上手](https://book.douban.com/subject/26836700/)


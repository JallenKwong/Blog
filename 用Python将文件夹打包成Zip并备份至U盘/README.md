# 用Python将文件夹打包成Zip并备份至U盘 #

creation date:2020-03-13 12: 23: 39

tag:Python, zip

## 需求概要 ##

将maven工程打包并备份至U盘。为了简单起见，只需备份工程中的src文件夹和pom.xml文件即可。

## 放码过来 ##

```python
import os
import zipfile
import datetime
import shutil

nowTimeStr = datetime.datetime.now().strftime("%Y%m%d%H%M")
newZipFileName = 'nice%s.zip' % nowTimeStr
newZip = zipfile.ZipFile(newZipFileName, 'w')

# pack the src folder
for folderName, subfolders, filenames in os.walk("."):
    
    if folderName.startswith('.\\src'):
        for filename in filenames:
            path = "%s\\%s"%(folderName, filename)
            print path
            newZip.write(path, compress_type=zipfile.ZIP_DEFLATED)
            

    if folderName == '.':
        for filename in filenames:
            if "pom.xml" == filename or "backup.py" == filename:
                path = "%s\\%s"%(folderName, filename)
                print path
                newZip.write(path, compress_type=zipfile.ZIP_DEFLATED)

newZip.close()     

#move zip to destination
backupPath = "E:\\Backup"

if not os.path.exists(backupPath):
    print "BackupPath: %s is not existed."%backupPath
else:
    shutil.move(newZipFileName, backupPath)
    print "Done"

raw_input()

```

## 参考资料 ##

[Python编程快速上手](https://book.douban.com/subject/26836700/)

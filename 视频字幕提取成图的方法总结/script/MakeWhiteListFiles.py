# -*- coding: UTF-8 -*-

# 作者：白居布衣
import os

whiteFileName = 'WhiteList.txt'

for item in os.listdir("."):
    if os.path.isdir(item):
        open("%s/%s"%(item, whiteFileName),"w").close()

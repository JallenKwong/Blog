# -*- coding: utf-8 -*

import os

l = [name for name in os.listdir('.') if name.endswith('jpg')]

out = open("Variables.js","w")
out.write("var ImageNameList = ")
out.write(str(l))
out.write("\n")

###

out.write("var videoNameList = ['拖延症.mp4']\n")

'''
l2 = [name.decode('gbk').encode('utf-8') for name in os.listdir('../Video') if name.endswith('mp4')]

out.write("var videoNameList = [")
temp = ""
for name in l2:
    temp += ("'../Video/" + name + "',")
    
out.write(temp[:-1] + "]\n")
'''
###

num = os.getcwd().split("\\")[-1]

out.write("var videoNameIndex = parseInt('%s') - 1" % num)
out.write("\n")

###

out.write("var aItemName = '%s_selectedList'\n" % num)


out.close()



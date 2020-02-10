# -*- coding: UTF-8 -*-

# 视频截图字幕缩叠
# 作者：白居布衣

from PIL import Image
import os, time

whiteListFileName = "WhiteList.txt"
imageSuffix = "jpg"
firstImageAllIn = False
developmentMode = False
cropHeight = 32 # 底部字幕的高度
offset = 0 #底部字幕右下坐标向上位移量

def containDir(path):
    for item in os.listdir(path):
        if os.path.isdir("%s/%s"%(path, item)):
            return True      
    return False

def mergeImage(folderName, imagenamelist, targetFolderName=None):
    whiteList = []
    if os.path.exists("%s/%s"%(folderName, whiteListFileName)):
        whiteList = [whiteitem.strip() for whiteitem in open("%s/%s"%(folderName, whiteListFileName)).readlines()]

    # 字符串默认排序图文件列表
    imagenamelist.sort()

    firstImage = Image.open("%s/%s" % (folderName, imagenamelist[0]))
    width, height = firstImage.size

    # 截取图的左上坐标，右下坐标(不包含)
    leftUp = (0, height - cropHeight)
    rightDown = (width, height - offset)

    imagelist = []

    #截取各图
    for imagename in imagenamelist:
        #print imagename
        im = Image.open("%s/%s" % (folderName, imagename))

        if imagenamelist.index(imagename) == 0 and firstImageAllIn or imagename in whiteList:
            imagelist.append(im.crop((0, 0, rightDown[0], rightDown[1])))
            continue
        
        imagelist.append(im.crop((leftUp[0], leftUp[1], rightDown[0], rightDown[1])))

    #开始合并
    newImageHeight = sum([im.size[1] for im in imagelist])    
    newImage = Image.new('RGB', (width, newImageHeight))

    countHeight = 0
    for im in imagelist:
        newImage.paste(im.copy(),(0, countHeight))
        countHeight += im.size[1]

    # 保存图片
    if targetFolderName is None:
        newImage.save("%s/%s"%(folderName, 'result.%s'%imageSuffix))
    else:
        now = str(int(round(time.time())))
        filename = "%s/%s"%(targetFolderName, 'result_%s.%s'%(now,imageSuffix))
        while os.path.exists(filename):
            now = str(int(round(time.time())))
            filename = "%s/%s"%(targetFolderName, 'result_%s.%s'%(now,imageSuffix))
        newImage.save(filename)

#--main--
targetFolderName = "result"
if not os.path.exists(targetFolderName):
    os.makedirs(targetFolderName)

count = 0

for item in os.listdir("."):

    if developmentMode and count > 0:
        continue
    
    if os.path.isdir(item) and not item.startswith("result") :
        
        print "---%s---"%item
        # 二级子目录的图片合并
        if containDir(item):
            print "%s contains subdir."%item
            for item2 in os.listdir(item):
                print "----%s----"%item2
                path = "%s/%s"%(item, item2)
                mergeImage(path, [imagename for imagename in os.listdir(path) if imagename.endswith(imageSuffix)], targetFolderName)
                print
        else:
            print "%s does not contain subdir."%item
            mergeImage(item, [imagename for imagename in os.listdir(item) if imagename.endswith(imageSuffix)], targetFolderName)
        print

    if developmentMode:
        count+=1
print "Done."


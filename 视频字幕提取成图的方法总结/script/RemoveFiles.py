import os
import shutil

filename = ''

for name in os.listdir('.'):
    if name.startswith('PrepareToDelete'):
        filename = name
        break

if filename == '':
    exit()

infile = open(filename)

content = infile.readline()

exec 'fileNameList=' + content

#print str(fileNameList)

garbageFolderName = "garbage"

if not os.path.exists(garbageFolderName):
    os.mkdir(garbageFolderName)

for name in fileNameList:

    print "Move %s to %s/%s."%(name, garbageFolderName, name)

    if not os.path.exists(name):
        print "%s is not existed." % name
        continue
    
    shutil.move(name, "%s/%s"%(garbageFolderName, name))

print "Done."

raw_input()
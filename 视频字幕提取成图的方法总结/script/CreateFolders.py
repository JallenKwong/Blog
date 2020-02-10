import os

num = 0


while True:
    print "How many folder would you create?"

    numStr = raw_input()

    try:
        num = int(numStr)
    except Exception as err:
        print "Exception ignored: " + str(err)
        continue

    if num < 5:
        print "At least 5."
        continue
    else:
        break



for i in range(num):

    folderName = ''

    if i + 1 < 10:
        folderName = '0' + str(i + 1)
    else:
        folderName = str(i + 1)

    if os.path.exists(folderName) is False:
        os.mkdir(folderName)

print "Done!"

raw_input()





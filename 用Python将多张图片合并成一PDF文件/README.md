# 用Python将多张图片合并成一PDF文件 #

creation date:2020-02-06 15: 04: 16

tag:Python, PDF

## 先前条件 ##

需要安装两模块：`fpdf`、`PIL`

- `pip install fpdf`
- `pip install PIL`


## 放码过来 ##

```python
from fpdf import FPDF
from PIL import Image
import os

def makePdf(pdfFileName, listPages):

    cover = Image.open(listPages[0])
    width, height = cover.size

    pdf = FPDF(unit = "pt", format = [width, height])

    for page in listPages:
        pdf.add_page()
        pdf.image(page, 0, 0)

    pdf.output(pdfFileName, "F")

makePdf("result.pdf", [imgFileName for imgFileName in os.listdir('.') if imgFileName.endswith("png")])
```

## 参考文献 ##

[Create PDF from a list of images](https://stackoverflow.com/questions/27327513/create-pdf-from-a-list-of-images)

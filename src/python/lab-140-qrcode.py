#
# filename    : lab-140-qrcode.py
# Description : QRCode Generator
# Docs        :
#               * https://pypi.org/project/qrcode/
# Requirements:
#               * pip install qrcode
#

import qrcode
img = qrcode.make('Some data here')
type(img)  # qrcode.image.pil.PilImage
img.save("file-18-qrcode-of-string.png")

filename = 'lab-140-qrcode.py' 
with open(filename, 'r') as file:
    lines = file.readlines()
    file_content = ''.join(lines).replace('\n','\\n')

img = qrcode.make(file_content)
img.save('file-19-qrcode-file-content.png')

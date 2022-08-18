import requests

import io
url='https://pixiv.shuia.tk/img-master/img/2022/08/17/21/00/07/100559621_p0_master1200.jpg'
image = requests.get(url).content
#image = open('lyf.jpg', 'rb').read()

image_b = io.BytesIO(image).read()
size = len(image_b)
mb=size/1024/1024
if mb>=1:
	print('ok')
print(mb)
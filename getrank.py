#爬pixiv 2022.8.18
import requests
import json
import time
import io
from bs4 import BeautifulSoup
url='https://www.pixiv.net/ranking.php?mode=daily_r18&content=illust&p=2&format=json'
headers={
  "Host": "www.pixiv.net",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:103.0) Gecko/20100101 Firefox/103.0",
  "Accept": "application/json",
  "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
  "Accept-Encoding": "gzip, deflate, br",
  "x-user-id": "82876637",
  "Sec-Fetch-Dest": "empty",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Site": "same-origin",
  "Referer": "https://www.pixiv.net/discovery",
  "Connection": "keep-alive",
  "Cookie": "first_visit_datetime_pc=2022-08-18+19%3A14%3A48; PHPSESSID=82876637_0ZtrwIThNkpfG6EEwm0ErDIo3X2YX5Pn; p_ab_id=8; p_ab_id_2=3; p_ab_d_id=1953423945; yuid_b=FHVEOJc; __cf_bm=LRei69KmokMnu1RsIY6DKR0uNBUD2Y9lAZ8j9NTCY9Q-1660817710-0-AW4soH4vh3vLTk3t9rkJafMOPXvi7pXXYpuWLBccmxheloigsF+srW+kjAarP/EdTDb3FFULmkHYZ/4dnl/Lt0DEvSQCMRYOSuq83Tla02RjJzuK1HuL2+oQVZS5NOtn0Oa7dIerqe/CgjLjcLg2o8/7oAWfdRcXxBhVyLz5dq5OfOSHZImKj6Y1UH77yHZc5g==; _ga_75BBYNYN9J=GS1.1.1660817699.1.1.1660818543.0.0.0; _ga=GA1.1.764569704.1660817700; _fbp=fb.1.1660817704825.1135456919; device_token=834de7dd183200935cbe12ab5fb888ae; privacy_policy_agreement=5; c_type=21; privacy_policy_notification=0; a_type=0; b_type=1; QSI_S_ZN_5hF4My7Ad6VNNAi=v:0:0; _im_vid=01GAR77G0GH589HAZVDFCYMDVF; login_ever=yes; _gcl_au=1.1.1188404511.1660817759",
  "TE": "trailers"
}
def getsize(url):
    image = requests.get(url).content
    image_b = io.BytesIO(image).read()
    size = len(image_b)
    mb=size/1024/1024
    print(mb)
    return mb
def get_durl(pid):
    pid=str(pid)
    pic_url = 'https://www.pixiv.net/artworks/' + pid
    rs = requests.get(pic_url, headers=headers)
    rs.encoding = 'UTF-8'
    bs = BeautifulSoup(rs.text, "html.parser")
    this = bs.select('#meta-preload-data')[0]['content']
    img = json.loads(this)['illust'][pid]['urls']
    ori=img['original']
    md=img['regular']
    img_url=ori
    img_url=img_url.replace('i.pximg.net','pixiv.shuia.tk')
    sizep=getsize(img_url)
    if(sizep>=1):
        md=md.replace('i.pximg.net','pixiv.shuia.tk')
        img_url=md
    return img_url
f=open('rankurl.txt','w')
f.write('')
f.close()
text=requests.get(url,headers=headers)
text=text.text
pjson=json.loads(text)
getp=pjson['contents']
leng=len(getp)
for i in range(leng):
	pid=getp[i]['illust_id']
	url=get_durl(pid)
	f=open('rankurl.txt','a+')
	f.write(url)
	f.write('\n')
	f.close()
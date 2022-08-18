import random
proxy='pixiv.shuia.tk'
f=open('../urls.txt','r')
t=f.read()
l=t.split('\n')
r=random.randint(0,len(l))
rr=l[r]
url=rr.replace('i.pximg.net',proxy)
print(url)
import random
f=open('../urls.txt','r')
t=f.read()
l=t.split('\n')
r=random.randint(0,len(l))
rr=l[r]
print(url)
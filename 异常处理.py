data={}
f=open(file=r'C:\Users\96978\Desktop\python\异常处理\baidu_x_system.log',mode='r')
for line in f.readlines():
	li=line.split()
	if li[0] in data:
		data[li[0]]+=1
	else:
		data[li[0]]=1
m=max(data,key=data.get)
print(m,data[m])
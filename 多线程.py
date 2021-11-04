import threading

import time
timer=0
basket=0#篮子
cashier=0#收银台
lock=threading.Lock()
class eggTart(threading.Thread):
	cooker=''#厨师
	count=0#计数
	def run(self) -> None:
		global timer
		global basket
		global cashier
		while timer<30:
			if basket>=500:
				lock.acquire()
				print('篮子已满')
				lock.release()
				time.sleep(3)
			else:
				self.count+=1
				basket=basket+1
				cashier-=1.5
				lock.acquire()
				print(self.cooker,'一共做了',self.count,'个','篮子里还有',basket,'个','工资为',round(self.count*1.5,1))
				lock.release()


class customer(threading.Thread):
	customer = ''  # 顾客
	wallet = 3000  # 顾客钱包
	cuscount=0#顾客买了多少个

	def run(self) -> None:
		global cashier
		global timer
		global basket
		while timer<30:

			if basket>0 and self.wallet>=3:
				self.wallet-=3
				self.cuscount+=1
				basket-=1
				cashier+=3
				lock.acquire()
				print(self.customer,'买了',self.cuscount,'个','还有',self.wallet,'元')
				lock.release()

			elif self.wallet<3:
				# lock.acquire()
				# print('余额不足')
				# lock.release()
				pass

			else:
				lock.acquire()
				print('已卖完，等待2秒')
				lock.release()
				time.sleep(2)





class Time(threading.Thread):
	def run(self) -> None:
		global cashier
		global timer
		while timer<30:
			time.sleep(1)
			timer+=1
			lock.acquire()
			print('还剩',30-timer,'秒')
			lock.release()
		print('盈利',cashier)



p1=eggTart()
p2=eggTart()
p3=eggTart()
p4=customer()
p5=customer()
p6=customer()
p7=customer()
p8=customer()
p9=customer()
timer1=Time()
p1.cooker='cooker1'
p2.cooker='cooker2'
p3.cooker='cooker3'
p4.customer='cus1'
p5.customer='cus2'
p6.customer='cus3'
p7.customer='cus4'
p8.customer='cus5'
p9.customer='cus6'

timer1.start()
p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
p6.start()
p7.start()
p8.start()
p9.start()
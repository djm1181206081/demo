"""
import xlrd

workbook = xlrd.open_workbook(
	filename=r'C:\Users\96978\Desktop\Python自动化测试\其他课程\python\day07\任务\2020年每个月的销售情况.xls')  # 替换文件路径，注意转换为.xls文件
# 全年的销售总额
# s=0
# for n in range(12):
# 	table= workbook.sheet_by_index(n)
# 	rows =table.nrows
# 	cols=table.ncols
# 	for row in range(1,rows):
# 		s+=round(table.cell_value(row,2),1)*int(table.cell_value(row,4))
# print('总销售额：',round(s,1))
# print('------------------------')

# 每件衣服的销售件数占比
# a={}
# sum=0
# for i in range(12):
# 	table= workbook.sheet_by_index(i)
# 	rows=table.nrows
# 	cols=table.ncols
# 	for row in range(1,rows):
# 		sum+=table.cell_value(row,4)
# 		if table.cell_value(row,1) not in a:
# 			a[table.cell_value(row,1)]=table.cell_value(row,4)
# 		else:
# 			a[table.cell_value(row,1)]+=table.cell_value(row,4)
# for j in a:
# 	print(j,'的销售件数占比为',format(a[j]/sum,'.2%'))
# print('------------------------')

# 每件衣服的月销售占比

# for i in range(12):
# 	table=workbook.sheet_by_index(i)
# 	rows=table.nrows
# 	cols=table.ncols
# 	a={}
# 	sum=0
# 	for row in range(1,rows):
# 		sum += table.cell_value(row, 4)
# 		if table.cell_value(row, 1) not in a:
# 			a[table.cell_value(row, 1)] = table.cell_value(row, 4)
# 		else:
# 			a[table.cell_value(row, 1)] += table.cell_value(row, 4)
# 	for j in a:
# 		print(j,'的',i+1,'月份占比为',format(a[j]/sum,'.2%'))
# 	print('------------------------')

# 每件衣服的销售额占比
# a={}
# s=0
# for n in range(12):
# 	table= workbook.sheet_by_index(n)
# 	rows =table.nrows
# 	cols=table.ncols
# 	for row in range(1,rows):
# 		s+=round(table.cell_value(row,2),1)*int(table.cell_value(row,4))
# 		if table.cell_value(row, 1) not in a:
# 			a[table.cell_value(row, 1)] = table.cell_value(row, 4)*round(table.cell_value(row,2),1)
# 		else:
# 			a[table.cell_value(row, 1)] += table.cell_value(row, 4)*round(table.cell_value(row,2),1)
# for j in a:
# 	print(j,'的销售额占比为',format(a[j]/s,'.2%'))
# print('--------------------------')

# 最畅销的衣服是那种
# 全年销量最低的衣服
# a={}
# for i in range(12):
# 	table=workbook.sheet_by_index(i)
# 	rows=table.nrows
# 	cols=table.ncols
# 	for row in range(1,rows):
# 		if table.cell_value(row, 1) not in a:
# 			a[table.cell_value(row, 1)] = table.cell_value(row, 4)
# 		else:
# 			a[table.cell_value(row, 1)] += table.cell_value(row, 4)
# print('最畅销的衣服是',max(a,key=a.get))
# print('全年销量最低的衣服是',min(a,key=a.get))
# print('------------------------')

# 每个季度最畅销的衣服
# def dictmax(dict,rows):
# 	for row in range(1, rows):
#
# 		if table.cell_value(row, 1) not in dict:
# 			dict[table.cell_value(row, 1)] = table.cell_value(row, 4)
# 		else:
# 			dict[table.cell_value(row, 1)] += table.cell_value(row, 4)
# 	return dict
#
# dict1={}
# dict2={}
# dict3={}
# dict4={}
# for i in range(12):
# 	table = workbook.sheet_by_index(i)
# 	rows = table.nrows
# 	cols = table.ncols
# 	if i==1 or i==2 or i==3:
# 		dict1=dictmax(dict1,rows)
# 	if i==4 or i==5 or i==6:
# 		dict2=dictmax(dict2,rows)
# 	if i==7 or i==8 or i==9:
# 		dict3=dictmax(dict3,rows)
# 	if i==10 or i==11 or i==0:
# 		dict4=dictmax(dict4,rows)
# print('第一季度最畅销的衣服为',max(dict1,key=dict1.get))
# print('第二季度最畅销的衣服为',max(dict2,key=dict2.get))
# print('第三季度最畅销的衣服为',max(dict3,key=dict3.get))
# print('第四季度最畅销的衣服为',max(dict4,key=dict4.get))
import xlrd

#调取excel表
wb=xlrd.open_workbook_xls(filename=r"C:\Users\TW\Desktop\day09\2020年每个月的销售情况.xlsx"，encoding_override=True)

#所有衣服
list=['羽绒服','牛仔裤','风衣','皮草','T血','马甲','小西装','衬衫','皮衣','休闲裤','卫衣','铅笔裤','棉衣']

#获取excel表中，所有工作簿名称
names=wb.sheet_names

#遍历出每个工作簿
for i in range(ien(names)):
     table=wb.sheet_by_(names[i])

#用角标遍历出每个工作簿
for i in range(12)
    teble=wb.sheet_by_name(name)
    return sheet

#读取工作簿内容
def sheet(name):
    sheet=wb.sheet_by_name(name)
    return sheet

#遍历出多少行
def rows(name):
    rows=sheet(neme).nrows
    return rows

#遍历出有多少列
def rows(name)
    rows=sheet(name).ncols
    return cols

#每个月的销售总额
def sum_month(name):
    sum=0
    for i in range(1,rows(name)):
        sum+=sheet(name).cell_value(i,2)*sheet(name).cell_value(i,4)
        return sum

#全年销售总额
def sum_year():
    sum=0
    for i in range(len(names)):
        sum+=sum_month(names[i])
        returm sum
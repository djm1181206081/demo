import random
print("********************************\n"
      "*                              *\n"
      "*   中国农业银行账户管理系统   *\n"
      "*                              *\n"
      "********************************\n"
      "*                              *\n"
      "*             选项             *\n"
      "*            1.开户            *\n"
      "*            2.存钱            *\n"
      "*            3.取钱            *\n"
      "*            4.转账            *\n"
      "*            5.查询            *\n"
      "*            6.Bye!            *\n"
      "*                              *\n"
      "********************************\n")
bank={}
bank_name="中国农业银行"
def bank_add(account,username,password,country,province,street,door):
    if account in  bank:#判断重名
        return 2
    elif len(bank)>= 100:#100个用户限制
        return 3
    else:#正常添加
        bank[account]={
            "username":username,
            "password":password,
            "country":country,
            "province":province,
            "street":street,
            "door":door,
            "money":0,
            "bank_name":bank_name
        }
        return 1
def Useradd():
    account=random.randint(10000000,99999999)#账号随机产生的
    username=str(input("请输入您的姓名"))
    password=int(input("请输入您的密码"))
    print("下面请输入您的地址：")
    country=input("\t\t请输入您的国家")
    province=input("\t\t请输入您的省份")
    street=input("\t\t请输入您的街道")
    door=input("\t\t请输入您的门牌号")
    add=bank_add(account,username,password,country,province,street,door)
    if add ==3:
        print("用户库已满")
    elif add==2:
        print("用户已存在")
    elif add ==1:
        print("恭喜您添加用户成功，以下是您的账户信息：")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, bank[account]["money"], bank_name))
def moneysadd():
    add=int(input("请输入您的账号"))
    if add in bank:
        moneys = (input("请输入你存款的金额："))
        bank[add]['money'] = bank[add]['money']+int(moneys)
        print("存款成功!当前余额为:",bank[add]['money'])
    else :
        print("未找到您的账户，操作已取消!\n")
def moneygadd():
    add=int(input("请输入您的账号"))
    if add in bank:
        password=input("请输入您的密码：")
        if password == bank[add]['password']:
            print("您的账户余额为:",bank[add]['money'])
            moneyg=(input("请输入你的取款金额："))
            if bank[add]['money']>0 and bank[add]['money']>int(moneyg):
                bank[add]['money'] = bank[add]['money']-int(moneyg)
                print("取款成功!当前余额为:",bank[add]['money'])
            else:
                print("操作失败，您的余额不足以支持此次取款\n")
        else :
            print("密码错误，操作已取消\n")
    else:
        print("未找到您的账户，操作已取消!\n")
def moneyzadd():
    add=int(input("请输入您的账号"))
    if add in bank:
        password=input("请输入您的密码：")
        if password == bank[add]['password']:
            print("您的账户余额为:",bank[add]['money'])
            adds=int(input("请输入您要汇款的账户号"))
            if adds in bank:
                moneyz=input("请输入您汇款的金额")
                if bank[add]['money']>0 and bank[add]['money']>int(moneyz):
                    bank[add]['money']=bank[add]['money']-int(moneyz)
                    bank[adds]['money']=bank[adds]['money']+int(moneyz)
                    print("转账成功!您当前的账户余额为:",bank[add]['money'])
                else:
                    print("操作失败，您的余额不足以支持此次转账\n")
            else:
                print("未找到该账户，操作已取消!\n")
        else:
            print("密码错误，操作已取消\n")
    else:
        print("未找到您的账户，操作已取消!\n")
def nameseadd():
    add=int(input("请输入您的账号"))
    if add in bank:
        password=input("请输入您的密码：")
        if password==bank[add]['password']:
            print(bank[add])
        else:
            print("密码错误，操作已取消\n")
    else:
        ("该用户不存在!\n")
while True :
    index=input("请输入您要执行的操作编号")
    if index.isdigit():
        if int(index) == 1:
            Useradd()
        elif int(index) == 2:
            moneysadd()
        elif int(index) == 3:
            moneygadd()
        elif int(index) == 4:
            moneyzadd()
        elif int(index) == 5:
            nameseadd()
        elif int(index) == 6:
            break
        else:
            print("系统没有该编号的功能")
        else:
        print("请输入要操作的功能编号")
print('*****************************')
print('*       中国工商银行          *')
print('*       账号管理系统          *')
print('*          V1.0             *')
print('*****************************')
print('                             ')
print('*1.开户                       ')
print('*2.存钱                       ')
print('*3.取钱                       ')
print('*4.转账                       ')
print('*5.查询                       ')
print('*6.BYE!                      ')
print('*****************************')
dict = {}
otm = {}
while True:
    a=int(input('请输入你要进行的功能：'))
    if a==1:
        # dict = {}
        # whole={}
        # otm = {}
        '''添加用户'''
        import random
        num = random.randint(10000000, 100000000)
        num = str(num)
        name = input('请输入你的姓名：')
        '''检测密码是否输入zhengque'''
        for i in range(3):
            password = input('请输入你的密码(6位数字)：')
            if password.isdigit():
                if len(list(password)) != 6:
                    print('你输入的密码不符合要求')
                else:
                    break
            else:
                print('请输入数字')
        password = int(password)
        # address=input('请输入你的地址：')
        country = input('请输入国家：')
        province = input('请输入省份：')
        street = input('请输入街道：')
        house = input('请输入门牌号：')
        address = (country, province, street, house)
        money = int(input('请输入你的存款余额：'))
        yinhang = "中国工商银行的昌平支行"
        '''检测账号是否重复'''
        if num in dict:
            print('2，用户已存在')
        else:
            l = len(dict)
            whole = {}
            if l < 100:
                dict[str(num)] = password
                print('1，添加用户成功')
                print('你的账号：', num)
                print('你的密码：', password)
                print('你的姓名：', name)
                print('你的地址：', address)
                print('你的存款余额：', money)
                print('你的开户银行：', yinhang)
                whole['账号'] = num
                whole['密码'] = password
                whole['余额'] = money
                whole['你的地址'] = address
                whole['当前的账户的开户行'] = yinhang
                otm[num] = whole
                # print(otm)
                # print(dict)
            else:
                print('3，用户库已满')
    elif a==2:
        num = input('请输入你要存钱的账号：')
        if num in dict:
            money1 = int(input('请输入你要存的金额：'))
            money = money + money1
            otm[num]['余额']=money
            print(num in dict)
            print('账户余额为：', money)
        else:
            print(num in dict)
    elif a == 3:
        num = input('请输入你要取钱的账号：')
        # password=int(input('请输入你的密码：'))
        # money2=int(input('请输入你要取钱的金额：'))
        if num in dict:
            password = int(input('请输入你的密码：'))
            if password == dict[num]:
                money2 = int(input('请输入你要取钱的金额：'))
                if money > money2:
                    money = money - money2
                    otm[num]['余额'] = money
                    print('余额为:',money)
                else:
                    print('3，钱不够')
            else:
                print('2，密码不对')
        else:
            print('1，账号不存在')
    elif a == 4:
        num = input('请输入你要转出的账号：')
        if num in dict:
            password = int(input('请输入你的密码：'))
            if password == dict[num]:
                num1 = input('请输入你要转入的账号：')
                if num1 in dict:
                    pass
                else:
                    print('你要转入的账号不存在')
                money3 = int(input('请输入你要取钱的金额：'))
                if otm[num]['余额'] > money3:
                    money = otm[num]['余额'] - money3
                    otm[num]['余额']=money
                    otm[num1]['余额']=otm[num1]['余额']+money3
                    print('转账成功')
                    print('余额为:',money)
                else:
                    print('3，钱不够')
            else:
                print('2，密码不对')
        else:
            print('1，账号不存在')
    elif a == 5:
        num = input('请输入你要查询的账号：')
        password = int(input('请输入你的密码：'))
        if num in dict:
            if password == dict[num]:
                # print(otm[num])
                for key, value in otm[num].items():
                    print(key, ':', value)
            else:
                print('密码错误')
        else:
            print('该用户不存在')
    elif a == 6:
        break
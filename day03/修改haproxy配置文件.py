'''
修改haproxy配置文件
1、查
    输入：www.oldboy.org
    获取当前backend下的所有记录

2、新建
    输入：
        arg = {
            'backend': 'www.oldboy.org',
            'record':{
                'server': '100.1.7.9',
                'weight': 20,
                'maxconn': 3000
            }
        }

3、删除
    输入：www.oldboy.org
    删除当前backend下的所有记录
'''


def seq(na):
    '''
    根据给na网址，查出是否在文件中,返回判断值和结果
    '''
    f = open("seq_testfile.txt", "r", encoding="utf-8")
    data = []
    for i in f:
        data.append(i.strip())
    f.close()
    na = "backend " + na
    if na in data:
        seq_result = data[data.index(na) + 1]
        return 1, seq_result
    else:
        return 0, "没找到"


def new_data():
    '''
    新建数据，判断是否存在，不存在就新建，返回判断值
    '''
    args = []
    while True:
        arg = input()
        if arg.strip() == "":
            break
        args.append(arg.strip())
    arg = eval("".join(args).split("=")[1])
    n_data = ""
    for k, v in arg["record"].items():
        n_data += "%s %s " % (k, str(v))
    o_data = seq(arg["backend"])
    if o_data[0] == 1:
        print("已存在！")
    else:
        f = open("seq_testfile.txt", "a", encoding="utf-8")
        temp = "%s %s\n        %s %s %s %d %s %d" % (
            "backend", ar["backend"],
            "server", ar["record"]["server"],
            "weight", ar["record"]["weight"],
            "maxconn", ar["record"]["maxconn"])
        f.write("\n")
        f.write(temp)
        f.close()


def del_data():
    temp_addr = input("输入要删除的网址：")
    temp_addr = "backend " + temp_addr
    f = open("seq_testfile.txt", "r", encoding="utf-8")
    temp = ""
    for i in f:
        if i.startswith(temp_addr):
            f.readline()
            f.readline()
            continue
        temp += i
    f.close()
    f = open("seq_testfile.txt", "w", encoding="utf-8")
    f.write(temp)
    f.close()


while True:
    print(''' 
        1.查询：
        2.新建：
        3.删除：
        4.退出：
        ''')
    chooce = input("选择你要的操作：")
    if chooce == "1":
        net_addr = input("输入要查询的网址：")
        print(seq(net_addr))
    elif chooce == "2":
        print("输入新建的参数：")
        new_data()
    elif chooce == "3":
        del_data()
    elif chooce == "4":
        break


goods = []
sh_or_mer = input("商家入口按“1”，购物按“2”：")
if sh_or_mer == "2":
    shopping_car = []

    f = open("goodsmenu.txt", "r")
    salary = f.readline().strip().split(",")[1]
    if salary == "0":
        salary = int(input("请输入工资："))
    else:
        salary = int(salary)
    for good1 in f.readlines():
        goods.append(tuple(good1.strip().split(",")))
    f.close()

    while True:
        for k, good1 in enumerate(goods):
            print(k, good1)
        chooce = input("选择你想买的东西的货号,退出请按“q”：")
        if chooce == 'q':
            break
        elif int(chooce) < len(goods):
                chooce = int(chooce)
                price = int(goods[chooce][1])
                if salary >= price:
                    salary -= price
                    shopping_car.append(goods[chooce])
                    print("余额：", salary)
                else:
                    print("余额不足。。。。。。")
                    break
        else:
            print("你输入的货物不存在！")

    print("你购买的东西有：")
    for i in shopping_car:
        print(i)
    print("余额：", salary)
    f = open("goodsmenu.txt", "w")
    f.write("salary,%d %s" % (salary, '\n'))
    for good1 in goods:
        f.write("%s, %s%s" % (good1[0], good1[1], '\n'))
    f.close()

elif sh_or_mer == "1":
    f = open("goodsmenu.txt", "r")
    salary = f.readline()
    for good1 in f.readlines():
        goods.append(tuple(good1.strip().split(",")))
    f.close()
    while True:
        for k, good1 in enumerate(goods):
            print(k, good1)
        chooce = input("修改价格按选号，删除货品按“d”,"
                       "增加货物按“a”,退出请按“q”：")
        if chooce == 'q':
            break
        elif chooce == 'd':
            chooce = int(input("选择你要删除货物的序号："))
            print("已删除" + str(goods.pop(chooce)))
        elif chooce == 'a':
            item = input("请输入要增加的货物名称:")
            price = input("输入货物的价格:")
            goods.append((item, price))
        elif chooce.isdigit():
            if int(chooce) < len(goods):
                good1 = goods[int(chooce)][0]
                price = input("输入货物的价格:")
                del goods[int(chooce)]
                goods.append((good1, price))
            else:
                print("没有这个货物。")
        else:
            print("你输错，请重新。")
    f = open("goodsmenu.txt", "w")
    f.write(salary)
    for good1 in goods:
        print(good1)
        f.write("%s, %s%s" % (good1[0], good1[1], '\n'))
    f.close()

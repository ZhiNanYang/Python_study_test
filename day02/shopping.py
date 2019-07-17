goods = [("iphone xr", 10000),
         ("RedMi", 1599),
         ("Canon Printer", 496),
         ("新华字典", 19),
         ("clock", 26)
         ]

shopping_car = []
salary = int(input("请输入工资："))

while True:
    for good1 in goods:
        print(goods.index(good1), good1)
    chooce = input("选择你想买的东西的货号,退出请按“q”：")
    if chooce == 'q':
        break
    else:
        chooce = int(chooce)
        price = goods[chooce][1]
        if salary >= price:
            salary -= price
            shopping_car.append(goods[chooce])
            print("余额：", salary)
        else:
            print("余额不足。。。。。。")
            break

print("你购买的东西有：")
for i in shopping_car:
    print(i)
print("余额：", salary)

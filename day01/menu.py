data = {
    '北京': {
        "昌平": {
            "沙河": ["oldboy", "test"],
            "天通苑": ["链家地产", "我爱我家"]
        },
        "朝阳": {
            "望京": ["奔驰", "陌陌"],
            "国贸": {"CICC", "HP"},
            "东直门": {"Advent", "飞信"}
        },
        "海淀": {},
    },
    '山东': {
        "德州": {},
        "青岛": {},
        "济南": {}
    },
    '广东': {
        "东莞": {},
        "常熟": {},
        "佛山": {}
    }
}

while True:
    for i in data:
        print(i)
    choice1 = input('退出按“q”，或输入选项>>>:')
    if choice1 in data:
        while True:
            for i1 in data[choice1]:
                print('\t' + i1)
            choice2 = input('退出按“q”，返回按“b”，或输入选项>>>:')
            if choice2 in data[choice1]:
                while True:
                    for i2 in data[choice1][choice2]:
                        print('\t' * 2 + i2)
                    choice3 = input('退出按“q”，返回按“b”，或输入选项>>>:')
                    if choice3 in data[choice1][choice2]:
                        for i3 in data[choice1][choice2][choice3]:
                            print('\t' * 3 + i3)
                        choice4 = input('退出按“q”，返回按“b”>>>:')
                        if choice4 == 'b':
                            break
                        elif choice4 == 'q':
                            exit()
                    if choice3 == 'b':
                        break
                    elif choice3 == 'q':
                        exit()
            if choice2 == 'b':
                break
            elif choice2 == 'q':
                exit()
    if choice1 == 'q':
        exit()

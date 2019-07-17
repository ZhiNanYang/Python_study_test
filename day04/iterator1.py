def a():
    print("迭代开始：")
    while True:
        b = yield
        print(b)
        b += 1
b = a()
b.__next__()
for i in range(1, 10):
    b.send(i)

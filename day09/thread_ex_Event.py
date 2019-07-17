import threading
import time
import random


def light():
    if not event.isSet():
        event.set()  # wait就不阻塞 #绿灯状态
    count = 0
    while True:
        if count < 10:
            print('--green light on---')
        elif count < 13:
            print('-yellow light on---')
        elif count < 20:
            if event.isSet():
                event.clear()
            print('-red light on---')
        else:
            count = 0
            event.set()  # 打开绿灯
        time.sleep(1)
        count += 1


def car(n):
    while 1:
        time.sleep(random.randrange(10))
        if event.isSet():  # 绿灯
            print("car [%s] is running.." % n)
        else:
            print("car [%s] is waiting for the red light.." % n)


if __name__ == '__main__':
    event = threading.Event()
    Light = threading.Thread(target=light)
    Light.start()
    for i in range(3):
        t = threading.Thread(target=car, args=(i,))
        t.start()

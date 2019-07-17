import threading
import time


class Mytread(threading.Thread):
    """docstring for Mytread"thread.Thread def __init__(self, arg):
        super(Mytread,thread.Thread.__init__()
        self.arg = arg
    """

    def __init__(self, n):
        super(Mytread, self).__init__()
        self.n = n

    def run(self):
        k.acquire()
        global num
        num += 1
        print(num)
        time.sleep(1)
        k.release()

num = 0
k = threading.Lock()
t_list = []
for i in range(5):
    t = Mytread(i)
    t.start()
    t_list.append(t)
for t in t_list:
    t.join()

print("___ end.", num)

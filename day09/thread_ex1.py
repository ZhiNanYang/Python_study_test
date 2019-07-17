import threading
import time


def run(n):
    print("thread, %s start" % n)
    time.sleep(2)
    print("thread, %s end" % n)


t1 = threading.Thread(target=run, args=(1,))
t2 = threading.Thread(target=run, args=(2,))
t1.start()
t2.start()


'''
class Mytread(threading.Thread):
    """docstring for Mytread"thread.Thread def __init__(self, arg):
        super(Mytread,thread.Thread.__init__()
        self.arg = arg
    """

    def __init__(self, n):
        super(Mytread, self).__init__()
        self.n = n

    def run(self):
        print("thread, %s start" % self.n)
        time.sleep(2)
        print("thread, %s end" % self.n)

start_time = time.time()
t_list = []
for i in range(50):
    t = Mytread(i)
    t.setDaemon(True)
    t.start()
    t_list.append(t)

# for t in t_list:
    # t.join()

print("___ end.", threading.current_thread(), threading.active_count())
print(time.time() - start_time)
'''

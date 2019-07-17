import threading
import queue
import time

def producer():
    for i in range(10):
        q.put("骨头 %s" % i)

    print("开始等待所有的骨头被取走...")
    q.join()
    print("所有的骨头被取完了...")


def consumer(n):

    while q.qsize() > 0:

        print("%s 取到" % n, q.get())
        time.sleep(1)
        q.task_done()  # 告知这个任务执行完了


q = queue.Queue()
p1 = threading.Thread(target=producer)
p2 = threading.Thread(target=producer)
p1.start()
p2.start()
c1 = threading.Thread(target=consumer, args=("yzn",))

c2 = threading.Thread(target=consumer, args=("lh",))
c1.start()
c2.start()

from multiprocessing import Process, Pool
import time, os


def Foo(i):
    time.sleep(1)
    print("child:", os.getpid())
    return i + 100


def Bar(arg):
    print("-->exec done:", arg)
    print(os.getpid())

if __name__ == '__main__':
    print("main:", os.getpid())
    pool = Pool(3)

    for i in range(10):
        pool.apply(func=Foo, args=(i,))
        # pool.apply_async(func=Foo, args=(i,), callback=Bar)
    print("end")
    pool.close()
    pool.join()

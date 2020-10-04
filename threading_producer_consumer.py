
# 基础知识五、Python实现线程池之线程安全队列
# https://blog.csdn.net/wang_xiaowang/article/details/105933224

import threading, time, random

class ThreadSafeQueue(object):

    def __init__(self, max_size=0):
        self.queue = []
        self.max_size = max_size  # max_size为0表示无限大
        self.lock = threading.Lock()  # 互斥量
        self.condition = threading.Condition()  # 条件变量

    def size(self):
        """
        获取当前队列的大小
        :return: 队列长度
        """
        # 加锁
        self.lock.acquire()
        size = len(self.queue)
        self.lock.release()
        return size

    def put(self, item):
        """
        将单个元素放入队列
        :param item:
        :return:
        """
        # 队列已满 max_size为0表示无限大
        # if self.max_size != 0 and self.size() >= self.max_size:
        #     print("~~~ ThreadSafeException ~~~")
        #     return ThreadSafeException()

        # 加锁
        self.lock.acquire()

        self.queue.append(item)

        self.lock.release()

        self.condition.acquire()
        # 通知等待读取的线程
        self.condition.notify()
        self.condition.release()

        return item


    def pop(self, block=False, timeout=0):
        """
        从队列头部取出元素
        :param block: 是否阻塞线程
        :param timeout: 等待时间
        :return:
        """
        if self.size() == 0:
            print("~~~~"+str(self.size()))
            if block:
                print("bbbbbbblock")
                self.condition.acquire()
                self.condition.wait(timeout)
                self.condition.release()
            else:
                print("nnnnnnot block")
                return None

        # 加锁
        self.lock.acquire()
        item = None
        if len(self.queue):
            item = self.queue.pop()
        self.lock.release()

        return item


class ThreadSafeException(Exception):
    pass


if __name__ == '__main__':

    thread_queue = ThreadSafeQueue(10)

    def producer():
        while True:
            thread_queue.put(random.randint(0, 10))
            time.sleep(2)

    def consumer():
        while True:
            print('current time before pop is %d' % time.time())

            item = thread_queue.pop(block=True, timeout=3) # 这是最重要的点！！block=true 是为了被阻塞
            print('get value from queue is %s' % item)

            print('current time after pop is %d' % time.time())

    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


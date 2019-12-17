# -*- coding:utf-8 -*-
"""
1.daemon:守护，主线程结束，则强制杀死子线程
        sing_thread = threading.Thread(target=sing, daemon=True)
    注意：必须要在线程开始之前设置守护
        sing_thread1 = threading.Thread(target=sing)
        sing_thread1.setDaemon(True)
    为了线程安全，每一个线程安全，每一个线程都要设置为TRUE
2.阻塞主线程(使用前提是设置守护)
    a.卡时间点
    b.使用.join([time]),主线程会等待使用了join()方法的线程执行完成
        sing_thread.join()
3.自定义线程
    a.必须要重写run方法，绑定任务
    b.不能使用run方法，而要使用start方法
    c.如果传递参数则要重写init方法
        def __init__(self, count1, count2):
            self.count1 = count1
            self.count2 = count2
            super().__init__()
4.多线程共享数据变量
    a.使用全局变量
        但是会引起资源竞争,可以让线程协同步调,让多个线程有一个顺序
         使用join()
         设置互斥锁
        缺点：一旦使用了线程协同,会使效率变慢,是多线程变为但线程
    b.互斥锁
        1.创建锁 threading.Lock()
        2.给线程上锁
        3.释放锁
        好处：可以实现线程同步
        坏处：是效率变低，但是比使用join效率高，容易出现死锁
"""

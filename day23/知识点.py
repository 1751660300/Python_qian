# -*- coding:utf-8 -*-
"""
1.多任务
    并发：CPU数量小于任务数，通过调度算法，实现任务“一起”执行
    便是问题：怎么实现高并发：
        什么式并发，举例 服务器集群
    并行：CPU数量大于任务数量，任务一起执行
    进程：就是计算机中的每一个程序
        进程是系统的资源的调度单位
        是资源调度的最小单位
    线程：《计算机程序执行的流程》:每一个进程都有一个线程（主线程）
        cpu执行的是进程中的线程，先得到进程，再执行线程
2.多线程
    一个进程可以同时执行多个线程
    a.使用多线程
        两个模块 _thread threading
        threading模块底层封装了_thread,推荐使用threading
    b.导入模块
        import threading
        from threading import Thread
        传参：*：表示特别重要
             group：
            *target：执行的目标任务名
            *args：执行任务需要的参数，用元组封装
            *kwargs：传参，使用字典形式
             name：
    c.获取线程列表
        threading.enumerate() 获取当前活动线程列表
        threading.current_thread() 获取主线程
"""
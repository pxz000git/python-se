#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:Pxz
# @Time :2019/1/17 0017下午 6:29


import socket
import threading

"""
Python主程序当且仅当不存在非Daemon线程存活时退出。
Daemon设置为子线程是否随主线程一起结束，默认为False。如果要随主线程一起结束需要设置为True

如果某个子线程的daemon属性为False，主线程结束时会检测该子线程是否结束，如果该子线程还在运行，则主线程会等待它完成后再退出；
如果某个子线程的daemon属性为True，主线程运行结束时不对这个子线程进行检查而直接退出，同时所有daemon值为True的子线程将随主线程一起结束，而不论是否运行完成

服务器端虽然可以处理无限多个连接，但只能一个一个的处理，
后面的客户端连接只能等待前面的连接完成才能发送数据。要同时处理多个连接，可以使用多线程。
服务器端接收到新的连接后，开启一个线程处理新连接，主线程去建立下一个连接
"""


def tcp_server_thread():
    """
    服务器端多线程处理连接
    """
    ip = '127.0.0.1'
    port = 8005
    address = (ip, port)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(address)
    server_socket.listen(5)
    print("开始监听")

    while True:
        conn_socket, addr = server_socket.accept()
        print('host is %s port is %s ' % (addr[0], addr[1]))
        thread_name = threading.current_thread().getName()
        send_msg = 'from server and the name of thread  is %s' % thread_name
        t = threading.Thread(target=my_thread, args=(send_msg, conn_socket))
        t.daemon = True
        t.start()


def my_thread(send_msg, conn_socket):
    rec_msg = conn_socket.recv(1024)
    print('server has rev the message is %s' % rec_msg)

    conn_socket.sendall(bytes(send_msg, encoding='UTF-8'))

    conn_socket.close()


if __name__ == "__main__":
    tcp_server_thread()

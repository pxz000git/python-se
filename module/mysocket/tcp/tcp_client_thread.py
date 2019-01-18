#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:Pxz
# @Time :2019/1/18 0018上午 11:44

import socket
import threading


def client_tcp():
    c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = '127.0.0.1'
    port = 8005
    address = (ip, port)
    c_socket.connect(address)
    return c_socket


def run_thread(c_socket):
    thread_name = threading.current_thread().getName()
    msg = 'from client and the name of thread  is %s' % thread_name
    t = threading.Thread(target=my_thread, args=(msg, c_socket))
    # t.daemon = True
    t.start()


def my_thread(msg, c_socket):
    c_socket.sendall(bytes(msg, encoding='UTF-8'))
    rec_msg = c_socket.recv(1024)
    print(rec_msg)
    c_socket.close()


if __name__ == "__main__":
    for i in range(15):
        run_thread(client_tcp())

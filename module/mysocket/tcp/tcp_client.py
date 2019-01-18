#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:Pxz
# @Time :2019/1/17 0017下午 5:28

import socket


def client_tcp():
    c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = '172.18.22.2'
    port = 8005
    address = (ip, port)
    c_socket.connect(address)

    msg = 'this is tcp client'
    msg = bytes(msg, encoding='UTF-8')
    c_socket.sendall(msg)
    rec_msg = c_socket.recv(1024)
    print(rec_msg)

    c_socket.close()


if __name__ == "__main__":
    client_tcp()

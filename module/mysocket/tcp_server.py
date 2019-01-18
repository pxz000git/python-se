#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:Pxz
# @Time :2019/1/17 0017下午 5:28

import socket


def server_tcp():
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = ''
    port = 8005
    address = (ip, port)
    s_socket.bind(address)
    s_socket.listen(5)
    while True:
        conn_socket, addr = s_socket.accept()
        print(s_socket)
        print('host is %s port is %s ' % (addr[0], addr[1]))

        rec_msg = conn_socket.recv(1024)
        print('server has rev the message is %s' % rec_msg)

        send_msg = "this is tcp server"
        send_msg = bytes(send_msg, encoding='UTF-8')
        conn_socket.sendall(send_msg)
        print('the new socket is %s' % conn_socket)

        conn_socket.close()
    s_socket.close()


if __name__ == "__main__":
    server_tcp()

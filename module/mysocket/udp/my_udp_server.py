#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:Pxz
# @Time :2019/1/18 0018下午 1:39


import socket


def server_socket():
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s_socket.bind(('', 8006))
    while True:
        data, addr = s_socket.recvfrom(1024)
        print('接收到ip 是%s,端口是 %s的链接,数据是 %s' % (addr[0], addr[1], data))
        # address = {'ip': addr[0], 'port': addr[1]}
        # print('接收的ip是{ip},端口是{port}'.format(**address))
        msg = b'the message from server'
        s_socket.sendto(msg, addr)


if __name__ == "__main__":
    server_socket()

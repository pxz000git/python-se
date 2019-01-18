#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:Pxz
# @Time :2019/1/18 0018下午 1:43


import socket


def client_udp():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg = b'the message from client'
    address = ('127.0.0.1', 8006)
    client_socket.sendto(msg, address)
    rec_data, addr = client_socket.recvfrom(1024)
    addr = {'ip': addr[0], 'port': addr[1]}
    print('返回的ip是{ip},端口是{port}'.format(**addr))
    print('收到服务端的数据是{data}'.format(data=rec_data))
    client_socket.close()


if __name__ == "__main__":
    client_udp()

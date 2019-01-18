#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:Pxz
# @Time :2019/1/17 0017下午 5:04


import socket


def get_host_by_name():
    ip = socket.gethostbyname('www.baidu.com')
    # n = socket.gethostbyaddr('MS-20180213SFEZ')
    # ip_tup = socket.gethostbyaddr('172.18.22.2')
    # print(n)
    # print(ip)
    # print(ip_tup)
    return ip


def socket_client():
    """
    向百度发送get请求
    :return:
    """
    # 建立套接字
    s_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = get_host_by_name()
    # ip = '172.18.22.2'
    port = 80
    server = (ip, port)
    s_client.connect(server)
    send_msg = b'GET / HTTP/1.1\r\n\r\n'
    s_client.sendall(send_msg)
    rec_msg = s_client.recv(4096)
    print(rec_msg)
    s_client.close()


if __name__ == "__main__":
    # get_host_by_name()
    socket_client()

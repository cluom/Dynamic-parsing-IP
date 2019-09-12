#!/usr/bin/env python
# coding=utf-8

from get_ip import GetIP
from parser import Parser

import os
import time
import datetime
import requests


def ifNetworkConn():
    try:
        requests.get('http://txt.go.sohu.com/ip/soip', timeout=2)
    except:
        return False
    return True


if __name__ == "__main__":
    getip = GetIP()
    parser = Parser()

    if ifNetworkConn():
        ip = getip.get_ip()
        
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if parser.searchRecordToRR():
            parser.updateRecord()
            print(now + ' 记录更新成功!')
        else:
            parser.addRecord()
            print(now + ' 记录添加成功!')
        while ifNetworkConn():
            newIP = getip.get_ip()
            if ip != newIP:
                ip = newIP
                parser.updateRecord()
                print(now + ' 记录更新成功!')

            time.sleep(60)

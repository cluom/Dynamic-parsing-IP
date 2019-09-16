#!/usr/bin/env python
# coding=utf-8

from get_ip import GetIP
from parser import Parser

import os
import time
import json
import datetime
import requests


def ifNetworkConn():
    try:
        requests.get('http://txt.go.sohu.com/ip/soip', timeout=2)
    except:
        return False
    return True

def main():
    getip = GetIP()
    parser = Parser()
    delay = 60
    dir_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(dir_path, 'config.json')
    with open(file_path) as config_file:
        config_json = json.loads(config_file.read())
        delay = config_json.get('conn_args').get('delay')
        print(delay)
    
    if not delay:
        print('延时填写错误!')
        exit()

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

            time.sleep(delay)


if __name__ == "__main__":
    main()

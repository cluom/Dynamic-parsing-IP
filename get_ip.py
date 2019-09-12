#!/usr/bin/env python
# coding=utf-8

import requests
import re

class GetIP(object):

    def __init__(self):
        self.url = 'http://txt.go.sohu.com/ip/soip'
    
    def get_ip(self):
        response = requests.get(self.url)
        ip = re.findall(r'\d+.\d+.\d+.\d+',response.text)[0]
        return ip
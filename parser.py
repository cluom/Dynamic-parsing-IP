#!/usr/bin/env python
# coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkalidns.request.v20150109.AddDomainRecordRequest import AddDomainRecordRequest
from aliyunsdkalidns.request.v20150109.UpdateDomainRecordRequest import UpdateDomainRecordRequest
from aliyunsdkalidns.request.v20150109.DescribeDomainRecordsRequest import DescribeDomainRecordsRequest

import os
import json
from get_ip import GetIP


class Parser(object):

    def __init__(self):
        dir_path = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(dir_path, 'test_config.json')

        with open(file_path) as config_file:
            config_json = json.loads(config_file.read())
            accessKeyId = config_json.get('conn_args').get('accessKeyId')
            accessSecret = config_json.get('conn_args').get('accessSecret')
            self.domainName = config_json.get('record_args').get('domainName')
            self.RRKeyWord = config_json.get('record_args').get('RRKeyWord')
            if not accessKeyId:
                print('accessKeyId不能为空!')
                exit()
            elif not accessSecret:
                print('accessSecret不能为空!')
                exit()
            elif not self.domainName:
                print('domainName不能为空!')
                exit()
            elif not self.RRKeyWord:
                print('RRKeyWord不能为空!')
                exit()
            self.client = AcsClient(accessKeyId, accessSecret, 'cn-hangzhou')
            print()

    def searchRecordToRR(self):
        request = DescribeDomainRecordsRequest()
        request.set_accept_format('json')
        request.set_DomainName(self.domainName)
        request.set_RRKeyWord(self.RRKeyWord)

        response = self.client.do_action_with_exception(request)
        result = str(response, encoding='utf-8')

        # print(result)
        result_json = json.loads(result)
        # print(result_json.get('DomainRecords').get('Record')[0].get('RecordId'))
        self.recordId = result_json.get('DomainRecords').get('Record')[
            0].get('RecordId')
        return result

    def addRecord(self):
        getip = GetIP()

        request = AddDomainRecordRequest()
        request.set_accept_format('json')
        request.set_DomainName(self.domainName)
        request.set_RR(self.RRKeyWord)
        request.set_Type("A")
        request.set_Value(getip.get_ip())
        try:
            response = self.client.do_action_with_exception(request)
            result = str(response, encoding='utf-8')
            # print(result)

            result_json = json.loads(result)
            # print(result_json.get('RecordId'))
            self.recordId = result_json.get('RecordId')
            return True
        except:
            return False

    def updateRecord(self):
        getip = GetIP()

        request = UpdateDomainRecordRequest()
        request.set_accept_format('json')
        request.set_RecordId(self.recordId)
        request.set_RR(self.RRKeyWord)
        request.set_Type("A")
        request.set_Value(getip.get_ip())

        try:
            response = self.client.do_action_with_exception(request)

            return True
        except:
            return False

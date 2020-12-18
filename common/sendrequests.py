#!/usr/bin/env python
# _*_ coding:utf-8 _*_


import os
import json
import requests



class SendRequests():
    """发送请求数据"""
    def sendRequests(self,s,apiData):
        try:
            #从读取的表格中获取响应的参数作为传递
            method = apiData["method"]
            url = apiData["url"]
            if apiData["params"] == "":
                par = None
            else:
                par = eval(apiData["params"])
            if apiData["headers"] == "":
                h = None
            else:
                h = eval(apiData["headers"])
            if apiData["body"] == "":
                body_data = None
            else:
                body_data = eval(apiData["body"])
            type = apiData["type"]
            v = False
            if type == "data":
                body = body_data
            elif type == "json":
                body = json.dumps(body_data)
            else:
                body = body_data

            #发送请求
            re = s.request(method=method,url=url,headers=h,params=par,data=body,verify=v)
            return re
        except Exception as e:
            print(e)
if __name__ == '__main__':
    s=requests.session()
    data={'module': '查询订单', 'ID': 'tradeOrder_001', 'UseCase': '平台单号查询', 'url': 'http://v2.guanyierp.com/tc/trade/trade_order_header/data/list?_dc=', 'method': 'post', 'params': '', 'headers': '{"Content-Type": "application/x-www-form-urlencoded"}', 'body': 'dateType=0&beginTime=&endTime=&shopIds=&vipName=&separatorVip=&code=&separatorCode=&platformCode=20201213005&separatorPlatform=&mailNo=&separatorMailno=&hasInvoice=&refund=&approve=&financeReject=&assign=&delivery=&cancel=false&hold=&customQueryParamInfos=%5B%5D&sort=&page=1&start=0&limit=10', 'type': 'data', 'status': 200.0, 'message': '', 'result': '', ' testers': ''}
    re=SendRequests().sendRequests(s,data)
    print(re)

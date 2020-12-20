# -*- coding: utf-8 -*-
__author__ = 'amy'
__date__ = '2020/12/20 17:50'

import requests
import json


data = {"email":"152@qq.com", "pwd":"Yun@2019",  "redirectUrl": "http://v2.guanyierp.com/login",
        "webType": "main", "authCode": ""}


s=requests.session()
s.post(url='http://login.guanyierp.com/login/loginDispatch',json=data)
s.get(url='http://v2.guanyierp.com/index')



def trade_order_search():
    data = 'dateType=0&beginTime=&endTime=&shopIds=&vipName=&separatorVip=&code=&separatorCode=&platformCode=20201213005&separatorPlatform=&mailNo=&separatorMailno=&hasInvoice=&refund=&approve=&financeReject=&assign=&delivery=&cancel=false&hold=&customQueryParamInfos=%5B%5D&sort=&page=1&start=0&limit=10'
    headers={'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
}
    r = s.post(url='http://v2.guanyierp.com/tc/trade/trade_order_header/data/list?_dc=',
                      data=data,headers=headers)
    print(r)

trade_order_search()
print(s.cookies)


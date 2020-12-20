import requests
import json


data = {"email":"152@qq.com", "pwd":"Yun@2019",  "redirectUrl": "http://v2.guanyierp.com/login",
        "webType": "main", "authCode": ""}

def renLogin():
    s=requests.session()
    r = s.post(url='http://login.guanyierp.com/login/loginDispatch',json=data)
    return r.cookie
#     print(r.json())
#     print(r.cookies)
# #
renLogin()


# def info():
#     '''查看信息'''
#     # home_url = 'http://v2.guanyierp.com/index'
#     # requests.get(url=home_url, cookies=renLogin())
#     url = 'http://v2.guanyierp.com/tc/trade/trade_order_header/data/list?_dc=1608378080780'
#     data = 'dateType=0&beginTime=&endTime=&shopIds=&vipName=&separatorVip=&code=&separatorCode=&platformCode=20201213005&separatorPlatform=&mailNo=&separatorMailno=&hasInvoice=&refund=&approve=&financeReject=&assign=&delivery=&cancel=false&hold=&customQueryParamInfos=%5B%5D&sort=&page=1&start=0&limit=10'
#     hearders={'Content-Type': 'application/json; charset=UTF-8'}
#     requests.post(url=url, data=data, hearders=hearders,cookies=renLogin())
#     data = 'dateType=0&beginTime=&endTime=&shopIds=&vipName=&separatorVip=&code=&separatorCode=&platformCode=20201213005&separatorPlatform=&mailNo=&separatorMailno=&hasInvoice=&refund=&approve=&financeReject=&assign=&delivery=&cancel=false&hold=&customQueryParamInfos=%5B%5D&sort=&page=1&start=0&limit=10'
#     r = requests.post('http://v2.guanyierp.com/tc/trade/trade_order_header/data/list?_dc=',
#                       data=data,
#                       cookies=renLogin())
#     print(r.text)
#
# info()

# -*- coding: utf-8 -*-
__author__ = 'amy'
__date__ = '2020/12/20 17:50'

import requests
import json

data = {"email": "152@qq.com", "pwd": "Yun@2019", "redirectUrl": "http://v2.guanyierp.com/login",
        "webType": "main", "authCode": ""}

s = requests.session()
s.post(url='http://login.guanyierp.com/login/loginDispatch', json=data)
s.get(url='http://v2.guanyierp.com/index')


def trade_order_search():
    data = 'dateType=0&beginTime=&endTime=&shopIds=&vipName=&separatorVip=&code=&separatorCode=&platformCode=20201213005&separatorPlatform=&mailNo=&separatorMailno=&hasInvoice=&refund=&approve=&financeReject=&assign=&delivery=&cancel=false&hold=&customQueryParamInfos=%5B%5D&sort=&page=1&start=0&limit=10'
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
               }
    result = s.post(url='http://v2.guanyierp.com/tc/trade/trade_order_header/data/list?_dc=',
                    data=data, headers=headers)
    res = result.json()
    r = json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)
    print(r)


def add_tradeorder():
    '''
    1、发起get请求
    2、从get请求中拿到no_repeat_sumit_trade、token、uniqueTid的值
    3、将上面三个参数放到请求中
    4.响应
    :return:
    '''

    result = s.get(url='http://v2.guanyierp.com/tc/trade/trade_order_header/add')
    print(result.text)

    # data = {
    #     "id": "292480387036",
    #     "uniqueTid": "c073cc3642f141feb9d23e99deeeaebd",
    #     "token": "279a09a7-0250-4fac-a621-50851c7c055a",
    #     "currentFormId": "no_repeat_sumit_tradeOrderHeaderAddOrUpdate",
    #     "no_repeat_sumit_tradeOrderHeaderAddOrUpdate": "7add998f-8df4-4793-8c61-4ba4102eb1aa",
    #     "shopId": "268448506540",
    #     "vipId": "283046558865",
    #     "vipAgent": 0,
    #     "platformCode": "20201221001",
    #     "warehouseId": "284249856264",
    #     "businessManId": "",
    #     "expressId": "10007026",
    #     "postFee": "0.0000",
    #     "currencyId": "",
    #     "dealDate": 1608530751000,
    #     "orderTypeId": "48165431",
    #     "planDeliveryDate": "",
    #     "codFee": "0.0000",
    #     "otherServiceFee": "0.0",
    #     "taxAmount": "0.0000",
    #     "discountFee": "140.0000",
    #     "buyerMemo": "",
    #     "sellerMemoLate": "",
    #     "extendMemo": "",
    #     "allowRepeat": "true",
    #     "subType": "",
    #     "subTypeValue": "",
    #     "platformFlag": "0",
    #     "sellerMemo": "",
    #     "flagId": "0",
    #     "copyFlag": True,
    #     "tradeOrderDetailList": [{
    #         "picUrl": "",
    #         "itemCode": "sy001",
    #         "itemName": "芙丽芳丝洗面奶氨基酸系",
    #         "itemSimpleName": "芙丽芳丝洗面奶",
    #         "itemSkuId": "268455240108",
    #         "itemSkuCode": "001",
    #         "itemSkuName": "正常规格",
    #         "stockStatusName": "",
    #         "skuId": "268455252962",
    #         "itemId": "268455237515",
    #         "itemCategoryName": "促销测试",
    #         "platformItemName": "",
    #         "platformSkuName": "",
    #         "cancel": False,
    #         "shopName": "",
    #         "skuPid": "",
    #         "type": "Item",
    #         "qty": 1,
    #         "discount": "1.0",
    #         "combineDetailId": "",
    #         "presale": False,
    #         "bmsStatus": "",
    #         "itemUnitName": "枝",
    #         "cycle": "",
    #         "cycleStatus": "",
    #         "baseName": "",
    #         "assistCode": "",
    #         "assistName": "",
    #         "ratioStr": "",
    #         "ratio": 0,
    #         "roundType": 0,
    #         "point": 0,
    #         "id": "292480395979",
    #         "discountFee": 0,
    #         "postFee": 0,
    #         "saleableQty": "-1",
    #         "pickableQty": 0,
    #         "originPrice": 150,
    #         "price": 150,
    #         "originAmount": 150,
    #         "amount": 150,
    #         "costPrice": 82.1106,
    #         "note": "",
    #         "planDeliveryDate": "",
    #         "assistQty": ""
    #     }],
    #     "tradeOrderPaymentList": [{
    #         "payTypeName": "支付宝",
    #         "payTypeId": "10010349",
    #         "payCode": "",
    #         "account": "",
    #         "id": "292480374783",
    #         "payment": 10,
    #         "paytime": ""
    #     }],
    #     "tradeOrderInvoiceList": [],
    #     "receiverName": "杨晓慧",
    #     "receiverPhoneBlur": "135*****103",
    #     "receiverPhone": "135*****103",
    #     "receiverMobileBlur": "135*****103",
    #     "receiverMobile": "135*****103",
    #     "receiverZip": "",
    #     "areaId": "330106",
    #     "receiverAddress": "某某某大酒店",
    #     "vipRealName": "杨晓慧",
    #     "vipIdCard": "",
    #     "vipEmail": "",
    #     "distributionOrder": False,
    #     "syncPlatform": False
    # }
    # headers = {'Content-Type': 'application/json; charset=UTF-8'
    #            }
    # result = s.post(url='http://v2.guanyierp.com/tc/trade/trade_order_header/create',
    #                 data=data, headers=headers)
    # print(result.text)

def approve():
    data='currentFormId=no_repeat_sumit_tradeOrderHeaderApprove&no_repeat_sumit_tradeOrderHeaderApprove=867b4b8f-9cd9-40e4-908b-083bfe4b76f6&ids=292481261996'
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
               }
    result = s.post(url='http://v2.guanyierp.com/tc/trade/trade_order_approve/approve',
                    data=data, headers=headers)
    print(result.text)

add_tradeorder()
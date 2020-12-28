# -*- coding: utf-8 -*-
__author__ = 'amy'
__date__ = '2020/12/20 17:50'

import requests
import json
import re
import random
import string


class trade_order:
    def __init__(self,user_data):
        self.user_data = user_data
        self.platformCode = self.getRandChar()
        self.session = requests.session()  # 创建session实例
        self.session.post(url='http://login.guanyierp.com/login/loginDispatch', json=self.user_data)
        self.session.get(url='http://v2.guanyierp.com/index')

    def getRandChar(self):
        sample = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        return sample

    def get_index(self,url='http://v2.guanyierp.com/tc/trade/trade_order_header/add'):
        index_info={"token":"","uniqueTid":"","no_repeat_sumit_tradeOrderHeaderAddOrUpdate":""}
        re_html = self.session.get(url=url)
        re_str = re_html.content.decode('utf-8')
        token = re.findall('<input type="hidden" id="hidToken" name="token" value="(.+?)"/>', re_str)[0]
        uniqueTid = re.findall('<input type="hidden" name="uniqueTid" value="(.+?)"/>', re_str)[0]
        no_repeat_sumit_tradeOrderHeaderAddOrUpdate = \
            re.findall('<input type="hidden" name="no_repeat_sumit_tradeOrderHeaderAddOrUpdate" value="(.+?)"/>', re_str)[
                0]
        index_info["token"]=token
        index_info["uniqueTid"]=uniqueTid
        index_info["no_repeat_sumit_tradeOrderHeaderAddOrUpdate"]=no_repeat_sumit_tradeOrderHeaderAddOrUpdate
        return index_info


    def add_tradeorder(self):
        data = {
            "id": "",
            "uniqueTid": self.get_index()["uniqueTid"],
            "token": self.get_index()["token"],
            "currentFormId": "no_repeat_sumit_tradeOrderHeaderAddOrUpdate",
            "no_repeat_sumit_tradeOrderHeaderAddOrUpdate": self.get_index()["no_repeat_sumit_tradeOrderHeaderAddOrUpdate"],
            "shopId": "268448506540",
            "vipId": "283046558865",
            "vipAgent": 0,
            "platformCode": self.platformCode,
            "warehouseId": "284249856264",
            "businessManId": "",
            "expressId": "10007026",
            "postFee": "0.0000",
            "currencyId": "",
            "dealDate": 1608530751000,
            "orderTypeId": "48165431",
            "planDeliveryDate": "",
            "codFee": "0.0000",
            "otherServiceFee": "0.0",
            "taxAmount": "0.0000",
            "discountFee": "140.0000",
            "buyerMemo": "",
            "sellerMemoLate": "",
            "extendMemo": "",
            "allowRepeat": "true",
            "subType": "",
            "subTypeValue": "",
            "platformFlag": "0",
            "sellerMemo": "",
            "flagId": "0",
            "copyFlag": True,
            "tradeOrderDetailList": [{
                "picUrl": "",
                "itemCode": "sy001",
                "itemName": "芙丽芳丝洗面奶氨基酸系",
                "itemSimpleName": "芙丽芳丝洗面奶",
                "itemSkuId": "268455240108",
                "itemSkuCode": "001",
                "itemSkuName": "正常规格",
                "stockStatusName": "",
                "skuId": "268455252962",
                "itemId": "268455237515",
                "itemCategoryName": "促销测试",
                "platformItemName": "",
                "platformSkuName": "",
                "cancel": False,
                "shopName": "",
                "skuPid": "",
                "type": "Item",
                "qty": 1,
                "discount": "1.0",
                "combineDetailId": "",
                "presale": False,
                "bmsStatus": "",
                "itemUnitName": "枝",
                "cycle": "",
                "cycleStatus": "",
                "baseName": "",
                "assistCode": "",
                "assistName": "",
                "ratioStr": "",
                "ratio": 0,
                "roundType": 0,
                "point": 0,
                "id": "292480395979",
                "discountFee": 0,
                "postFee": 0,
                "saleableQty": "-1",
                "pickableQty": 0,
                "originPrice": 150,
                "price": 150,
                "originAmount": 150,
                "amount": 150,
                "costPrice": 82.1106,
                "note": "",
                "planDeliveryDate": "",
                "assistQty": ""
            }],
            "tradeOrderPaymentList": [{
                "payTypeName": "支付宝",
                "payTypeId": "10010349",
                "payCode": "",
                "account": "",
                "id": "292480374783",
                "payment": 10,
                "paytime": ""
            }],
            "tradeOrderInvoiceList": [],
            "receiverName": "杨晓慧",
            "receiverPhoneBlur": "13534567898",
            "receiverPhone": "13534567898",
            "receiverMobileBlur": "13534567898",
            "receiverMobile": "13534567898",
            "receiverZip": "",
            "areaId": "330106",
            "receiverAddress": "某某某大酒店",
            "vipRealName": "杨晓慧",
            "vipIdCard": "",
            "vipEmail": "",
            "distributionOrder": False,
            "syncPlatform": False
        }

        result = self.session.post(url='http://v2.guanyierp.com/tc/trade/trade_order_header/create', json=data)
        print(result.json())

    def trade_order_list(self):
        data = f'dateType=0&beginTime=&endTime=&shopIds=&vipName=&separatorVip=&code=&separatorCode=&platformCode={self.platformCode}&separatorPlatform=&mailNo=&separatorMailno=&hasInvoice=&refund=&approve=&financeReject=&assign=&delivery=&cancel=false&hold=&customQueryParamInfos=%5B%5D&sort=&page=1&start=0&limit=10'
        headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
                   }
        result = self.session.post(url='http://v2.guanyierp.com/tc/trade/trade_order_header/data/list?_dc=',
                                   data=data, headers=headers)
        res = result.json()
        r = json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)
        print(r)

    def trade_order_detail(self):
        data = f'dateType=0&beginTime=&endTime=&shopIds=&vipName=&separatorVip=&code=&separatorCode=&platformCode={self.platformCode}&separatorPlatform=&mailNo=&separatorMailno=&hasInvoice=&refund=&approve=&financeReject=&assign=&delivery=&cancel=false&hold=&customQueryParamInfos=%5B%5D&sort=&page=1&start=0&limit=10'
        headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
                   }
        result = self.session.post(url='http://v2.guanyierp.com/tc/trade/trade_order_header/data/list?_dc=',
                                   data=data, headers=headers)
        res = result.json()
        r = json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)
        print(r)


    def approve(self):
        data = 'currentFormId=no_repeat_sumit_tradeOrderHeaderApprove&no_repeat_sumit_tradeOrderHeaderApprove=867b4b8f-9cd9-40e4-908b-083bfe4b76f6&ids=292481261996'
        headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
                   }
        result = self.session.post(url='http://v2.guanyierp.com/tc/trade/trade_order_approve/approve',
                                   data=data, headers=headers)
        print(result.text)


if __name__ == '__main__':
    data = {"email": "152@qq.com", "pwd": "Yun@2019", "redirectUrl": "http://v2.guanyierp.com/login",
            "webType": "main", "authCode": ""}

    trade_order1 = trade_order(data)
    # print(trade_order1.get_index()["token"])
    # trade_order1.add_tradeorder()

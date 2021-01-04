#!/usr/bin/env python
# _*_ coding:utf-8 _*_


import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest,requests
import random
import string
import re
from testfile.RelyData import RelyData

class TestMaiSong(unittest.TestCase):
    """买就送"""
    @classmethod
    def setUpClass(cls) :
        cls.user_data ={"email": "152@qq.com", "pwd": "Yun@2019", "redirectUrl": "http://v2.guanyierp.com/login",
            "webType": "main", "authCode": ""}
        cls.platformCode = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        cls.session = requests.session()  # 创建session实例
        cls.session.post(url='http://login.guanyierp.com/login/loginDispatch', json=cls.user_data)
        cls.session.get(url='http://v2.guanyierp.com/index')

    @classmethod
    def tearDownClass(cls):
        pass


    def test_getaddtrade(self):
        url = 'http://v2.guanyierp.com/tc/trade/trade_order_header/add'
        re_html = self.session.get(url=url)
        re_str = re_html.content.decode('utf-8')
        token = re.findall('<input type="hidden" id="hidToken" name="token" value="(.+?)"/>', re_str)[0]
        uniqueTid = re.findall('<input type="hidden" name="uniqueTid" value="(.+?)"/>', re_str)[0]
        no_repeat_sumit_tradeOrderHeaderAddOrUpdate = \
            re.findall('<input type="hidden" name="no_repeat_sumit_tradeOrderHeaderAddOrUpdate" value="(.+?)"/>',
                       re_str)[0]
        self.assertEqual(re_html.status_code, 200)
        setattr(RelyData,"token",token)
        setattr(RelyData, "uniqueTid", uniqueTid)
        setattr(RelyData, "no_repeat_sumit_tradeOrderHeaderAddOrUpdate", no_repeat_sumit_tradeOrderHeaderAddOrUpdate)

    def test_addtrade(self):
        data = {
            "id": "",
            "uniqueTid": getattr(RelyData,"uniqueTid"),
            "token": getattr(RelyData,"token"),
            "currentFormId": "no_repeat_sumit_tradeOrderHeaderAddOrUpdate",
            "no_repeat_sumit_tradeOrderHeaderAddOrUpdate": getattr(RelyData,"no_repeat_sumit_tradeOrderHeaderAddOrUpdate"),
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
                "qty": 2,
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





if __name__=='__main__':
    suite=unittest.TestSuite()
    suite.addTest(TestMaiSong("test_getaddtrade"))
    suite.addTest(TestMaiSong("test_addtrade"))
    runner=unittest.TextTestRunner()
    runner.run(suite)

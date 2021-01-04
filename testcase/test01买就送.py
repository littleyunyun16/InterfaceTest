#!/usr/bin/env python
# _*_ coding:utf-8 _*_


import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest,requests
import random
import string

class mai_song(unittest.TestCase):
    """买就送"""
    def setUpClass(cls) :
        cls.user_data ={"email": "152@qq.com", "pwd": "Yun@2019", "redirectUrl": "http://v2.guanyierp.com/login",
            "webType": "main", "authCode": ""}
        cls.platformCode = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        cls.session = requests.session()  # 创建session实例
        cls.session.post(url='http://login.guanyierp.com/login/loginDispatch', json=cls.user_data)
        cls.session.get(url='http://v2.guanyierp.com/index')


    def tearDownClass(cls):
        pass


    def test_addtrade(self,data):



if __name__=='__main__':
    unittest.main()

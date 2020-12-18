import requests

# post(url, data=None, json=None, **kwargs):


data = {"email": "152@qq.com", "pwd": "Yun@2019", "kaptcha": "", "redirectUrl": "http://v2.guanyierp.com/login",
        "webType": "main", "authCode": ""}


def renLogin():

    r = requests.post(url='http://login.guanyierp.com/login/loginDispatch',data=data)
    # return r.cookies
    print(r.status_code)


# def info():
#     '''查看信息'''
#     data = {'month': '7', 'requestToken': '-505719466', '_rtk': 'ad9c53b0'}
#     r = requests.post('http://sc.renren.com/scores/loadBornInfo',
#                       data=data,
#                       cookies=renLogin())
#     print(r.text)
#
#
# info()

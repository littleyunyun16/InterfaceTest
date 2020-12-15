import json
import hashlib



def get_sign(data):
    # str = json.dumps(data).replace(" ", "")
    str=json.dumps(data, separators=(',', ':'))
    secret = "82b2a0d77e37424ab76e5d8a3d5a1888"
    signss = secret + str + secret  # 拼接在一起
    m1 = hashlib.md5()  # md5转换，下面都是md5加密的用法
    m1.update(signss.encode(encoding='utf-8'))
    sign = m1.hexdigest().upper()  # 16进制输出，且字母是大写的
    return sign


if __name__ == '__main__':
    data ={
        "method": "gy.erp.trade.deliverys.get",
        "sessionkey": "94ee1ca3c41d44989290d02985105865",
        "appkey": "116761",
        "code": "SDO12508595405",
        "page_no": "1",
        "page_size": "10",
    }
    sign=get_sign(data)
    print(sign)

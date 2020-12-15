# 读取配置文件的方法，并返回文件的内容
import os
import configparser
import getpathinfo

path = getpathinfo.get_path()
config_path = os.path.join(path, 'testfile','config.ini')
config = configparser.ConfigParser()   # 前面的configparser是某文件名，ConfigParser()是configparser的一个类
config.read(config_path, encoding='utf-8')


class ReadConfig():

    def get_http(self, name):
        value = config.get('HTTP', name)
        return value

    def get_email(self, name):
        value = config.get('EMAIL', name)
        return value

    def get_mysql(self, name):
        value = config.get('DATABASE', name)
        return value


if __name__ == '__main__':  # 测试一下，我们读取配置文件的方法是否可用
    print('HTTP中的baseurl值为：', ReadConfig().get_http('baseurl'))
    print('EMAIL中的开关on_off值为：', ReadConfig().get_email('on_off'))
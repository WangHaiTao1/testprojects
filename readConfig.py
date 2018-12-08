import os
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]#当前路径
configPath = os.path.join(proDir, "config.ini")
# print(configPath)
class ReadConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(str(configPath),encoding="utf-8")
    def get_url(self,name):
        value = self.cf.get("HTTP",name)
        return value
    def get_headers(self,name):
        value = self.cf.get("HEADERS",name)
        return value
    def get_host(self,name):
        value = self.cf.get("HOST",name)
        return value


import os
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")


class ReadConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)
    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value
    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value

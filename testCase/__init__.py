import requests
import unittest
from common import readConfig
cf = readConfig.ReadConfig()
def setParameters():
    http = cf.get_http("scheme")
    baseurl = cf.get_http("baseurl")
    url = str(http) + str(baseurl) \
               + "/api/v1/cfuser/sendCode/13052395885"
    return url
print(setParameters())
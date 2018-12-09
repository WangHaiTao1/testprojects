# import requests
# import readConfig
# from public import commo
# url = readConfig.ReadConfig().get_url("baseurl")
# host = readConfig.ReadConfig().get_host("codehost")
# pathdir = readConfig.ReadConfig().get_host("xlsxhost")
# caseList = commo.get_xlsx(pathdir+"userCase.xlsx","sendcode")
# mobile = caseList[0][1]
# url1 = url+host+str(mobile)
# print(url)
# print(host)
# print(url1)
# re = requests.post(url=url1)
#
# print(re.json())
# print(re.text)

import unittest #单元测试框架
import paramunittest
@paramunittest.parametrized(
    [1,2],
    [3,4],
    [5,6]
)
class test(unittest.TestCase):
    def setParameters(self,a,b):
        print("我是用例1")
        self.a = a
        self.b = b
    def test2(self):
        print(self.a,self.b)
if __name__ == '__main__':
    unittest.main()
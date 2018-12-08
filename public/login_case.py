import requests
import unittest
import paramunittest
from  public import commo
import readConfig
import json
cf = readConfig.ReadConfig()
head = cf.get_headers("head")
print(head)
path = cf.get_host("xlsxHost")
get_xlsx = commo.get_xlsx(path+"userCase.xlsx","sendcode")
@paramunittest.parametrized(*get_xlsx)
class loginCase(unittest.TestCase):

    def  setParameters(self,case_name,mobile):
        """
        :param case_name:
        :param mobile:
        :return:
        """
        self.case_name = str(case_name)
        self.mobile = str(mobile)

    def setUp(self):
        print(self.case_name+"测试开始")

    def test_login_case(self):
        """set url 设置URL"""
        url = cf.get_url("baseurl")+\
              cf.get_host("codeHost")+\
              str(self.mobile)
        print(url)

        """set head 设置请求头"""
        headers = cf.get_headers("head")

        """send requests 发送请求"""

        self.re = requests.post(url=url)
        josn = self.re.json()
        data = josn["value"]
        success = josn["errorDescription"]
        error = josn["errorDescription"]
        mobileError = josn["errorDescription"]
        if data != None and success == '':
            self.assertEqual(1,1)
        elif error == "1000003":
            assert  error,"1000003"  "手机号为空"
            self.assertEqual(1,1)
        elif mobileError == "1000000" :
            assert error, "1000000"  "手机号错误"
            self.assertEqual(1,1)
        else:
            self.assertEqual(1,2)
    def tearDown(self):
        print(self.mobile)
        print(self.re.json())
        print("测试结束")

if __name__ =='__main__':
    unittest.main()
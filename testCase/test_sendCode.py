import requests#请求
import unittest
import readConfig
import paramunittest
from common import comm
login_xls = comm.get_xls("userCase.xlsx","login")
print(login_xls)
cf = readConfig.ReadConfig()

@paramunittest.parametrized(*login_xls)
class testCode(unittest.TestCase):

    def setParameters(self,case_name,email):
        """
        set params
        :param case_name
        :param email
        :return:
        """
        self.case_name = case_name
        self.email = email
    def setUp(self):
        print("***********testSendCode-测试开始**********")

    def test_SendCode_success(self):
        url=cf.get_http("baseurl")+"/api/v1/cfuser/sendCode/"+self.email
        self.re = requests.post(url)
        self.data = self.re.json()
        self.assert_code()
    def assert_code(self):

        self.value = str(self.data["value"])
        self.code=self.value.split("! ")[-1]
        self.assertEqual(self.re.status_code,200)
        self.assertEqual(self.re.ok,True)
        self.assertEqual(self.data["success"],True)
    def tearDown(self):

        print(self.code)
        print(self.value)
        print("**************测试结束*************")


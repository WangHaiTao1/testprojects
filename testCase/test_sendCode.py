import requests
import unittest
from common import readConfig
cf = readConfig.ReadConfig()
class testCode(unittest.TestCase):

    def setParameters(self):
        self.http =cf .get_http("scheme")
        self.baseurl = cf.get_http("baseurl")
        self.url = str(self.http)+str(self.baseurl) \
                    +"/api/v1/cfuser/sendCode/13052395885"
        return self.url
    def setUp(self):
        print("***********testSendCode-测试开始**********")

    def test_SendCode_success(self):
        self.re = requests.post(self.setParameters())
        self.data = self.re.json()
        self.assert_code()
    def assert_code(self):

        self.value = str(self.data["value"])
        self.code=self.value.split("! ")[-1]
        self.assertEqual(self.re.status_code,200)
    def tearDown(self):

        print(self.code)
        print(self.value)
        print("**************测试结束*************")

if __name__ == "__main__":
    unittest.main()
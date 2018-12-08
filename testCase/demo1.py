import unittest
import paramunittest
from common import comm
get_xls = comm.get_xls("userCase.xlsx","login")
print(get_xls)
@paramunittest.parametrized(*get_xls)
class test(unittest.TestCase):
    def setParameters(self,case_name,email):
        """
        set params
        :param case_name
        :param email
        :return:
        """
        self.case_name = str(case_name)
        self.email = str(email)

    def setUp(self):
        print(self.case_name+"开始")

    def test_test(self):
        print(self.email)
    def tearDown(self):
        print("结束")

# @paramunittest.parametrized(
#  ["asdasda","asdsadsa","fasfasfsa"]
# )
# class TestFoo(paramunittest.ParametrizedTestCase):
#     def setParameters(self, a, b,c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def testLess(self):
#         print(self.a,self.b)
#         self.assertLess(self.a, self.b)


if __name__ =="__main__":
    unittest.main()
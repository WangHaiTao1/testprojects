import requests  #引用request模块
""""""


# """60秒内"""
# re = requests.post(url)  #使用request模块里的post请求方式
# data=re.json() # 获取josn类型的response
# print(data)
# """错误手机号"""
# re = requests.post(url1)  #使用request模块里的post请求方式
# data=re.json() # 获取josn类型的response
# print(data)
# code = re.status_code #获取响应状态码
# text = re.text   #获取响应文本
# url = re.url  #获取请求URL
# encoding = re.encoding #获取编码格式
# header=re.headers# 获取请求头内容
# ok = re.ok # 获取请求结果
# raw = re.raw # 获取结果raw文本格式
url = "https:" \
      "//m-test.ibubuji.com" \
      "/api/v1/cfuser/sendCode/" \
      "13127996352"
"""正确手机号  接受发送验证码"""
re = requests.post(url)  #使用request模块里的post请求方式
data=re.json() # 获取josn类型的response
code = str(data["value"]).split("! ")[-1]
print(data)


"""登录请求"""
import json
headers = {"Content-Type":"application/json"}
params = json.dumps({
	"mobile": "13127996352",
	"code": code,
	"cid": "",
	"did": "",
	"url": ""
})

url1 = "https://m-test.ibubuji.com/api/v1/cfuser/login/mobile"
dlqq = requests.post(url=url1,headers=headers,data=params)
token = dlqq.json()["token"]
print(token)

"""查询收货地址"""
url2 = "https://m-test.ibubuji.com/api/v1/cfcrowd/product/presale/list"
head = {"Authorization":token,"Content-Type":"application/json"}
shdz = requests.get(url=url2,headers=head)
print(shdz.json())
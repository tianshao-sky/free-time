# http://lbsyun.baidu.com/index.php?title=webapi
import requests

url = 'http://api.map.baidu.com/place/v2/suggestion'
params = { 'query' : '浙江大学',
           'region': '杭州',
           'ak' : '',          # 百度密钥
           'output': 'json'     }          # 输出结果设置为json格式
res = requests.get(url,params)
json_ = res.content.decode('utf-8')
print(json_)

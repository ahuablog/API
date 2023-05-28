import json
import requests

TIP = "https://api.threatbook.cn/v3/scene/ip_reputation"
apiKey = "apikey"
item = input("输入您的IP：")


reqUrl = "{}?apikey={}&resource={}&lang=zh".format(TIP,apiKey,item)
req = requests.get(reqUrl)
resp = json.loads(req.text)

info = resp['data']['{}'.format(item)]

if req.status_code == 200:
    judgments = info['judgments']
    severity = info['severity']
    carrier = info['basic']['carrier']
    location = info['basic']['location']

    print("风险级别:",severity)
    print("威胁标签:",judgments)
    print("地址所属:",carrier)
    print("地理位置:",location)
    print("原始内容:",resp)


else:
    print(resp.status_code)

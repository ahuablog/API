import requests
import json

# 钉钉机器人的 Webhook 地址
webhook_url = "https://oapi.dingtalk.com/robot/send?access_token=tokenkey"

# 发送消息的函数
def send_message(msg):
    headers = {"Content-Type": "application/json;charset=utf-8"}
    data = {"msgtype": "text", "text": {"content": msg},"at":{"atMobiles":[13071609551]}}
    r = requests.post(webhook_url, headers=headers, data=json.dumps(data))
    return r.json()

# 测试发送消息
send_message("【告警信息】梓淦和志淋都是我小弟! ")

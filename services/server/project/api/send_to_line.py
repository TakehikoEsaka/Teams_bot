# -*- coding:utf-8 -*-
import urllib.parse as p
import urllib.request as r
import urllib.error as e
import json
import os

url = 'https://api.line.me/v2/bot/message/push'
channel_access_token = str(os.getenv("CHANNEL_ACCESS_TOKEN"))
user_id = str(os.getenv("USER_ID"))

def send_message(message):
    # 送信用のデータ
    data = {
        'to' : user_id,
        'messages' : [
            {
                'type' : 'text',
                'text' : message
            }
        ]
    }
    # byte型にencode必要
    jsonstr = json.dumps(data).encode("utf-8")
    request = r.Request(url, data=jsonstr)
    request.add_header('Content-Type', 'application/json')
    request.add_header('Authorization', 'Bearer ' + channel_access_token)
    request.get_method = lambda: 'POST'

    # 送信実行
    response = r.urlopen(request)
    ret = response.read()
    print('Response:', ret)


if __name__ == '__main__':
    send_message("おはよう")
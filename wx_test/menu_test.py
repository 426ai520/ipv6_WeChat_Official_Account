# -*- encoding: utf-8 -*-

import urllib.request
from urllib.parse import urlencode
import json
import sys
import importlib

importlib.reload(sys)

appid = 'wxb596c90e795d46b3'
secret = 'f6bc8c361cb46bd8b4dc227ad01e3201'

gettoken = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=' + appid + '&secret=' + secret

f = urllib.request.urlopen(gettoken)

stringjson = f.read()

access_token = json.loads(stringjson)['access_token']
print(access_token)

posturl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=" + access_token

menu = '''''{ 
     "button":
        [
            {
                "name": "校区1",
                "sub_button":
                [
                    {
                        "type": "view",
                        "name": "浴室",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
                    },
                    {
                        "type": "view",
                        "name": "水房",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
                    }
                ]
            },
            {
                "name": "校区2",
                "sub_button":
                [
                    {
                        "type": "view",
                        "name": "浴室",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
                    },
                    {
                        "type": "view",
                        "name": "水房",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
                    }
                ]
            },
            {
                "type": "click",
                "name": "其他",
                "key": "mpGuide"
            }
          ] 
 }'''

request = urllib.request.urlopen(posturl, menu.encode('utf-8'))

print(request.read())
# -*- coding: utf-8 -*-
# filename: menu.py

import urllib.request
from basic import Basic

class Menu(object):
    def __init__(self):
        pass
    def create(self, postData, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % accessToken
        if isinstance(postData, str):
            postData = postData.encode('utf-8')
        urlResp = urllib.request.urlopen(url=postUrl, data=postData)
        print(urlResp.read())

    def query(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/get?access_token=%s" % accessToken
        urlResp = urllib.request.urlopen(url=postUrl)
        print(urlResp.read())

    def delete(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s" % accessToken
        urlResp = urllib.request.urlopen(url=postUrl)
        print(urlResp.read())

    #获取自定义菜单配置接口
    def get_current_selfmenu_info(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/get_current_selfmenu_info?access_token=%s" % accessToken
        urlResp = urllib.request.urlopen(url=postUrl)
        print(urlResp.read())

if __name__ == '__main__':
    myMenu = Menu()
    postJson = """
    {
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
    }
    """
    accessToken = "21_N4utMh-fLj5jXr4WI4ADp9jk2PwSx3b1w6Nf4y1leniuRDjBjVm7GXx9js8gqw272OWlSe3kYl5PkXsVmXUSzcEAZTPPD5UDsRy3rV8B94sExPNVRnthU7BZpHMV5x-Y6sD_c3fUIbNdSgaCIYThAAACSN"
    # myMenu.delete(accessToken)
    myMenu.create(postJson, accessToken)
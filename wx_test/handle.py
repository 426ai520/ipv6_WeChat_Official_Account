# coding:utf-8
# fiename: handle.py

# import hashlib
import reply
import receive
import db_test
import web

class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return 'hello, this is a test'
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = 'gkx_wx'

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            sha1.update(list[0].encode("utf-8"))
            sha1.update(list[1].encode("utf-8"))
            sha1.update(list[2].encode("utf-8"))
            hashcode = sha1.hexdigest()  # 获取加密串
            # map(sha1.update, list) # 官网这个有问题
            print('test/GET func: hashcode, signature:', hashcode, signature)
            if hashcode == signature:
                return echostr
            else:
                return
        except Exception as Argument:
            return Argument

    def POST(self):
        try:
            webData = web.data()
            print("Handle Post webdata is ", webData)
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'text':
                    rec_text = recMsg.Content.decode('utf-8')
                    print('the input is: ', rec_text)
                    content = db_test.reply_result(rec_text) # 调用查询数据库程序
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                if recMsg.MsgType == 'image':
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()
                if recMsg.MsgType == 'event':
                    event = recMsg.Event
                    if event == 'subscribe':  # 判断如果是关注则进行回复
                        content = "您好，欢迎关注！发送数字‘1’即可获得当前浴室排队情况；发送数字‘2’即可获得当前水房排队情况。"
                        replyMsg = reply.TextMsg(toUser, fromUser, content)
                        return replyMsg.send()
            else:
                print("暂且不处理")
                return "success"
        except Exception as Argment:
            return Argment

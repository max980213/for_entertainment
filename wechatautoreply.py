from wxpy import *
import json
import requests
import datetime

bot=Bot(cache_path=True)  # 登录微信，括号里是缓存，不用每次运行都登录

friends=bot.friends()
friendslist=[]
for one in friends:
    friendslist.append(one.name)

# 创建还有列表
'''
for one in friendslist:
    try:
        print(one)
    except:
        print('no')
        continue
'''

@bot.register()

def recv_send_msg(recv_msg):
    print(recv_msg.sender)
    if recv_msg.sender.name in friendslist:
        #print('收到了来自 %s 的消息，他说： %s ' % recv_msg.sender,recv_msg.text)
        print('收到的消息：',recv_msg.text)
        now_time=datetime.datetime.now()
        string='现在是： '+str(now_time)
        return '：我是正在测试的自动回复，'+string
    else:
        pass

embed()

# 非常短 因此功能极少
# 它会对收到的任何消息进行回复，包括群消息和公众号消息。
# 在python3.6.8下运行，所以你需要安装一个python3.6.8
# 或者你把它变成可执行文件

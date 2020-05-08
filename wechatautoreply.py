from wxpy import *
import json
import requests
import datetime

bot=Bot(cache_path=True)  # 登录微信，括号里是缓存，短时间内不用每次运行都登录

@bot.register()

def recv_send_msg(recv_msg):
        print('收到的消息：',recv_msg.text)
        now_time=datetime.datetime.now()
        string='现在是： '+str(now_time)
        return '我是正在测试的自动回复，'+string  # 该位置是自动回复的内容

embed()

# 非常短 因此功能极少
# 它会对收到的任何消息进行回复，包括群消息和公众号消息。
# 在python3.6.8下运行，所以你需要安装一个python3.6.8
# 或者你把它变成可执行文件

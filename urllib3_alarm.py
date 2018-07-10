#encoding:utf-8
import urllib3.request
import json
import time

corpid = 'ww17c02156145616b3'
corpsecret = 'SOs0R0G9b9lvSYd5dA3y2LANEJ5qtFA3EhJV-arVRNo'
url = 'https://qyapi.weixin.qq.com'
msg ='网络连接异常，请马上检查网络连接，防止掉线'
#--------------------------------
# 获取企业微信token
#--------------------------------

def get_token(url, corpid, corpsecret):
    token_url = '%s/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (url, corpid, corpsecret)
    token = json.loads(urllib3.request.urlopen(token_url).read().decode())['access_token']
    return token

#--------------------------------
# 构建告警信息json
#--------------------------------
def messages(msg):
    values = {
        "touser": '@all',
        "msgtype": 'text',
        "agentid": 1000003, #最好使用变量
        "text": {'content': msg},
        "safe": 0
        }
    msges=(bytes(json.dumps(values), 'utf-8'))
    return msges

#--------------------------------
# 发送告警信息
#--------------------------------
def send_message(url,token, data):
        send_url = '%s/cgi-bin/message/send?access_token=%s' % (url,token)
        respone=urllib3.request.urlopen(urllib3.request.Request(url=send_url, data=data)).read()
        x = json.loads(respone.decode())['errcode']
        # print(x)
        if x == 0:
            print ('Wechat message send Succesfully')
        else:
            print ('Wechat message send Failed')

##############函数结束########################

#网络测试定义

def net_ping1():
    import os
    return1=os.system('ping 192.168.2.1 -n 1')
    if return1:
        print ('ping fail')
        #调用系统网络诊断
        #os.system('msdt.exe /id NetworkDiagnosticsNetworkAdapter')
        #微信函数调用
        test_token=get_token(url, corpid, corpsecret)
        msg_data= messages(msg)
        send_message(url,test_token, msg_data)
    else:
        print ('ping')


#系统的联网监测
# def net_ping2():
#     import os
#     import subprocess
 
#     fnull = open(os.devnull, 'w')
#     return1 = subprocess.call('ping 8.8.8.8', shell = True, stdout = fnull, stderr = fnull)
#     if return1:
#         return1 = subprocess.call('msdt.exe /id NetworkDiagnosticsNetworkAdapter', shell=True, stdout=fnull, stderr=fnull)
#         print ('ping fail')
#     else:
#         print ('ping ok')
#     fnull.close()

#循环任务
def loop_ping():
     count = 1
     while count > 0:
     	time.sleep(5)
     	net_ping1()
     	timenow = time.time()
     	count += 1
     	print (timenow,count)

if __name__=='__main__':
    loop_ping()

def net_test1():
    import os
    return1=os.system('ping 192.168.2.1 -n 1')
    if return1:
        print ('ping fail')
        os.system('msdt.exe /id NetworkDiagnosticsNetworkAdapter')#调用系统网络诊断
    else:
        print ('ping')
def net_test2():
    import os
    import subprocess
 
    fnull = open(os.devnull, 'w')
    return1 = subprocess.call('ping 8.8.8.8', shell = True, stdout = fnull, stderr = fnull)
    if return1:
        return1 = subprocess.call('msdt.exe /id NetworkDiagnosticsNetworkAdapter', shell=True, stdout=fnull, stderr=fnull)
        print ('ping fail')
    else:
        print ('ping ok')
    fnull.close()
 
if __name__=='__main__':
    net_test1()

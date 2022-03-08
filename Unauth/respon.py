import webbrowser
import time
import requests
import threading
start=time.time()
headers={
'User-Agent':"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
'Connection':'close'
}
def result():
    a = open('tes.txt', 'r', encoding='utf-8')
    f = a.read().splitlines()  # 读取文件去掉换行符
    for readline in f:
            url=readline
            response=requests.get(url=url,headers=headers)
            if response.status_code==200:
                    if url[-3:]=="php":
                        with open ('php.txt','a+') as f:
                            f.writelines(url+'\n')
                    elif url[-4:] == "html":
                        with open('html.txt', 'a+') as f:
                            f.writelines(url + '\n')
                    elif url[-2:]=="js":
                        with open ('js.txt','a+') as f:
                            f.writelines(url+'\n')
                    # webbrowser.open(url)
                    else:
                        pass
            elif response.status_code==403:
                with open('403.txt','a+')as f:
                    f.writelines(url+'\n')
            else:
                pass
                print (str(response.status_code)+":"+url)
t1=threading.Thread(target=result())
t1.start()

# if __name__ == "__main__":
#     t1=threading.Thread(target=result())
#     t1.start()
#     end=time.time()
#     print ("所用时间为:%s"%(end-start))
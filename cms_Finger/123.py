import aiohttp
import asyncio
import random
import json
import time
import datetime
import warnings
import sys


warnings.filterwarnings("ignore",category=DeprecationWarning) #消除版本警告


startscaning=datetime.datetime.now()  #开始扫描的时间
start=time.time()


def title():
    print('+------------------------------------------+')
    print('+  \033[34mTitle: 星光指纹识别                     \033[0m+')
    print('+  \033[36m使用格式:  python3 poc.py url           \033[0m+')
    print('+  \033[36mUrl         >>> http://xxx.xxx.xxx.xxx  \033[0m+')
    print('+  \033[31mBy:ATeam                                \033[0m+')
    print('+------------------------------------------+\n')
def requests_headers():
    user_agent = ['Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.8.1) Gecko/20061010 Firefox/2.0',
    'Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.6 Safari/532.0',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1 ; x64; en-US; rv:1.9.1b2pre) Gecko/20081026 Firefox/3.1b2pre',
    'Opera/10.60 (Windows NT 5.1; U; zh-cn) Presto/2.6.30 Version/10.60','Opera/8.01 (J2ME/MIDP; Opera Mini/2.0.4062; en; U; ssr)',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; ; rv:1.9.0.14) Gecko/2009082707 Firefox/3.0.14',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows; U; Windows NT 6.0; fr; rv:1.9.2.4) Gecko/20100523 Firefox/3.6.4 ( .NET CLR 3.5.30729)',
    'Mozilla/5.0 (Windows; U; Windows NT 6.0; fr-FR) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16',
    'Mozilla/5.0 (Windows; U; Windows NT 6.0; fr-FR) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5']
    UA = random.choice(user_agent)
    headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent':UA,
    'Upgrade-Insecure-Requests':'1','Connection':'keep-alive','Cache-Control':'max-age=0',
    'Accept-Encoding':'gzip, deflate, sdch','Accept-Language':'zh-CN,zh;q=0.8',
    "Referer": "http://www.baidu.com/link?url=www.so.com&url=www.soso.com&&url=www.sogou.com",
    'Cookie':"PHPSESSID=gljsd5c3ei5n813roo4878q203"}
    return headers


class cms():
    def __init__(self,url):
        self.url=url
        self.config_file="data.json"
        self.thread=100
        self.headers=requests_headers()
        self.flag=0
        asyncio.run(self.aio_main())
        if not self.flag:
            print("\033[31m[+]\033[0m 未检测到cms")

    async def async_scan(self,i):
        client=aiohttp.ClientSession()
        while True:
            if self.queue.empty():
                break
            else:
                try:
                    _url=self.queue.get_nowait()
                    urls=self.url+_url[0]
                    response=await client.get(urls,headers=self.headers)
                    await response.release()
                    if response.status==200:
                        nowtime = datetime.datetime.now().strftime('%H:%M:%S')
                        print(f'\033[35m[{nowtime}]\033[0m  {urls}-----------\033[31m[+]{_url[1]}\033[0m')
                        self.flag+=1
                        break
                except:
                    pass
        await client.close()

    # 协程任务列表
    async def aio_main(self):
        self.queue = asyncio.PriorityQueue()
        await self.load_dic()
        tasks=[self.async_scan(i) for i in range(self.thread)]
        done,pending=await asyncio.wait(tasks,timeout=None)

    #字典读取
    async def load_dic(self):
        with open(self.config_file) as f:
            cfg=json.load(f)
        for x in cfg:
            url_list=x['url'].split(',')
            for Af in url_list:
                await self.queue.put((Af,x['name']))

    #批量文件读取
def load_urls():
    with open('url.txt','r')as f:
        data=f.readlines()
    return data

if __name__=="__main__":
    title()
    print("\033[32m[+]Start scanning:%s\033[0m\n" % startscaning)
    if len(sys.argv) == 1:
        url_list = load_urls()
        for lurl in url_list:
            cms(lurl.strip())
            print(lurl)
    else:
        url = sys.argv[1]
        cms(url)
    end=time.time()
    endscaning=datetime.datetime.now()
    print("\n\033[32m[+]End Scanning:%s\033[0m" % endscaning)
    print("\033[32m[+]Total Time:%s\033[0m\n"%(end-start))
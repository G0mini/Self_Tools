import  re
import requests
from bs4 import BeautifulSoup as bs
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Upgrade-Insecure-Requests':'1'
}
def iplist(): #http://www.66ip.cn/
    ip_port = [];
    for x in range(1,30):
        url=r'http://www.66ip.cn/{}.html'.format(x)
        html=requests.get(url=url,headers=headers)
        html=html.text.encode("latin1").decode('gbk') #中文乱码解决
        re_ip=re.findall("((?:[0-9]{1,3}\.){3}[0-9]{1,3})",html) # ip正则匹配
        re_port=re.findall("<td>(\d{1,5})</td>",html) #port正则匹配
        result=dict(zip(re_ip,re_port)) #列表合成字典
        for key in result: #字典遍历
            ip_port.append(key+":"+result[key])
    return ip_port

def iplist2():#https://www.89ip.cn/
    a=[]
    url='https://www.89ip.cn/tqdl.html?api=1&num=100'
    iplist2get=requests.get(url=url,headers=headers).text
    re_ip2=re.findall('((?:[0-9]{1,3}\.){3}[0-9]{1,3}.*?\d{1,5})',iplist2get)
    for x in re_ip2:
        a.append(x)
    return a

def ver(ips):
    for ip in ips:
        proxies={
            'http':'http://{}'.format(ip),
            'https':'https://{}'.format(ip)
        }
        url='http://www.baidu.com'
        try:
            res=requests.get(url=url,proxies=proxies,timeout=1)
            if res.status_code == 200:
                print('Success:'+ip)
                with open('Success.txt','a+') as f:
                    f.write(ip+'\n')
        except Exception as e:
            print ('Failed:'+ip)

def result():
    ips=iplist2()
    ver(ips)
    ips=iplist()
    ver(ips)


if __name__=='__main__':
    result()

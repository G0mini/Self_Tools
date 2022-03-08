import requests
import argparse
import sys
import base64
import json
import prettytable as pt
import threading
import time
import re

start = time.time()
fofa_email = ''  # fofa邮箱
fofa_key = ''  # fofa API_Key
fofa_country = '&&country="CN"'
fofa_url = f'https://fofa.so/api/v1/search/all?&email={fofa_email}&key={fofa_key}'
qax_username = 'G0mini'
qax_key = ''  # qax默认10天更新一次。
qax_url = f'https://hunter.qianxin.com/openApi/search?&username={qax_username}&api-key={qax_key}&country=="中国"'


def banner():
    print(

        '''
          ______     ______            _
         / ____/    / ____/___  ____ _(_)___  ___  _____
        / / __     / __/ / __ \/ __ `/ / __ \/ _ \/ ___/
       / /_/ /    / /___/ / / / /_/ / / / / /  __(__  )
       \____/____/_____/_/ /_/\__, /_/_/ /_/\___/____/
           /_____/           /____/                      By:G0mini
           '''

    )


def domain():
    export = open('domain.txt', 'w+', encoding='utf-8')
    export1 = []
    export2 = []
    do = sys.argv[2]
    endo = f'domain="{do}"'
    fofa_qbase64 = base64.b64encode(endo.encode('utf-8') + fofa_country.encode('utf-8'))
    fofa_params = {
        'qbase64': fofa_qbase64,
    }
    fofa_response = requests.get(url=fofa_url, params=fofa_params)
    fofa_data = json.loads(fofa_response.text)
    print(fofa_data)
    for i in fofa_data['results']:
        patter = re.compile('[0-9]')
        match = patter.findall(i[0])
        if "https" not in i[0]:
            if match:
                export1.append('http://' + i[0])
            else:
                export1.append('http://' + i[0] + ":" + i[2])
        else:
            if match:
                export1.append(i[0])
            else:
                export1.append(i[0] + ":" + i[2])

    qax_search = base64.b64encode(endo.encode('utf-8')).decode('utf-8')
    page = sys.argv[3]
    page_size=(int(page)*10)
    qax_params = {
        'search': qax_search,
        'page': page,
        'page_size':page_size
    }
    time.sleep(2)
    qax_response = requests.get(url=qax_url, params=qax_params)
    qax_data = json.loads(qax_response.text)
    try:
        for result in qax_data['data']['arr']:
            export1.append(result['url'])
    except:
        pass
    for final in export1:
        if final not in export2:
            export2.append(final)
    for finresult in export2:
        export.write(finresult + '\n')
        print(finresult)
    export.close()


def body():
    export = open('body.txt', 'w+', encoding='utf-8')
    export1 = []
    export2 = []
    do = sys.argv[2]
    endo = f'body="{do}"'
    fofa_qbase64 = base64.b64encode(endo.encode('utf-8') + fofa_country.encode('utf-8'))
    fofa_params = {
        'qbase64': fofa_qbase64,
    }
    fofa_response = requests.get(url=fofa_url, params=fofa_params)
    fofa_data = json.loads(fofa_response.text)
    for i in fofa_data['results']:
        patter = re.compile('[0-9]')
        match = patter.findall(i[0])
        if "https" not in i[0]:
            if match:
                export1.append('http://' + i[0])
            else:
                export1.append('http://' + i[0] + ":" + i[2])
        else:
            if match:
                export1.append(i[0])
            else:
                export1.append(i[0] + ":" + i[2])

    qax_search = base64.urlsafe_b64encode(endo.encode('utf-8'))
    page = sys.argv[3]
    page_size=(int(page)*10)
    qax_params = {
        'search': qax_search,
        'page': page,
        'page_size':page_size
    }
    time.sleep(2)
    qax_response = requests.get(url=qax_url, params=qax_params)
    qax_data = json.loads(qax_response.text)
    try:
        for result in qax_data['data']['arr']:
            export1.append(result['url'])
    except:
        pass
    for final in export1:
        if final not in export2:
            export2.append(final)
    for finresult in export2:
        export.write(finresult + '\n')
        print(finresult)
    export.close()


def app():
    export = open('app.txt', 'w+', encoding='utf-8')
    export1 = []
    export2 = []
    do = sys.argv[2]
    endo = f'app="{do}"'
    fofa_qbase64 = base64.b64encode(endo.encode('utf-8') + fofa_country.encode('utf-8'))
    fofa_params = {
        'qbase64': fofa_qbase64,
    }
    fofa_response = requests.get(url=fofa_url, params=fofa_params)
    fofa_data = json.loads(fofa_response.text)
    for i in fofa_data['results']:
        patter = re.compile('[0-9]')
        match = patter.findall(i[0])
        if "https" not in i[0]:
            if match:
                export1.append('http://' + i[0])
            else:
                export1.append('http://' + i[0] + ":" + i[2])
        else:
            if match:
                export1.append(i[0])
            else:
                export1.append(i[0] + ":" + i[2])

    qax_search = base64.b64encode(endo.encode('utf-8')).decode('utf-8')
    page = sys.argv[3]
    page_size=(int(page)*10)
    qax_params = {
        'search': qax_search,
        'page': page,
        'page_size':page_size
    }
    time.sleep(2)
    qax_response = requests.get(url=qax_url, params=qax_params)
    qax_data = json.loads(qax_response.text)
    try:
        for result in qax_data['data']['arr']:
            export1.append(result['url'])
    except:
        pass
    for final in export1:
        if final not in export2:
            export2.append(final)
    for finresult in export2:
        export.write(finresult + '\n')
        print(finresult)
    export.close()


def ip():
    export = open('ip.txt', 'w+', encoding='utf-8')
    export1 = []
    export2 = []
    do = sys.argv[2]
    endo = f'ip="{do}"'
    fofa_qbase64 = base64.b64encode(endo.encode('utf-8') + fofa_country.encode('utf-8'))
    print(fofa_qbase64)
    fofa_params = {
        'qbase64': fofa_qbase64,
    }
    fofa_response = requests.get(url=fofa_url, params=fofa_params)
    print(fofa_response.text)
    fofa_data = json.loads(fofa_response.text)
    for i in fofa_data['results']:
        patter = re.compile('[0-9]')
        match = patter.findall(i[0])
        if "https" not in i[0]:
            if match:
                export1.append('http://' + i[0])
            else:
                export1.append('http://' + i[0] + ":" + i[2])
        else:
            if match:
                export1.append(i[0])
            else:
                export1.append(i[0] + ":" + i[2])

    qax_search = base64.b64encode(endo.encode('utf-8')).decode('utf-8')
    print(qax_search)
    page = sys.argv[3]
    page_size=(int(page)*10)
    qax_params = {
        'search': qax_search,
        'page': page,
        'page_size':page_size
    }
    time.sleep(2)
    qax_response = requests.get(url=qax_url, params=qax_params)
    print(qax_response.text)
    qax_data = json.loads(qax_response.text)
    try:
        for result in qax_data['data']['arr']:
            export1.append(result['url'])
    except:
        pass
    for final in export1:
        if final not in export2:
            export2.append(final)
    for finresult in export2:
        export.write(finresult + '\n')
        print(finresult)
    export.close()

if __name__ == '__main__':
    banner()
    parser = argparse.ArgumentParser("""fofa与qax_Hunter的api调用,自行添加key
        用法:
        python3 GApi.py -d xxx.com 3(页码)
        python3 GApi.py -b xxx.js 3(页码)
        python3 GApi.py -a xxOA 3(页码)
        python3 GApi.py -i 127.0.0.1 3(页码)""")
    parser.add_argument("-d", "--domain", dest='domain', help="子域名查询", nargs='*')
    parser.add_argument("-b", "--body", dest='body', help="特征查询", nargs='*')
    parser.add_argument("-a", "--app", dest='app', help="特定cms/设备查询", nargs='*')
    parser.add_argument("-i", "--ip", dest='ip', help="IP查询", nargs='*')
    args = parser.parse_args()
    if args.domain:
        domain()
    elif args.body:
        body()
    elif args.app:
        app()
    elif args.ip:
        ip()

    end = time.time()
    print("time:%s" % (end - start))
#coding:utf-8
import re
import sys
import json
with open(sys.argv[1],encoding='utf-8') as f:
    ALLEXE = json.loads(f.read())
with open(sys.argv[2],encoding='ISO-8859-1') as f:
    tasklist = f.read()

class SP:
    def __init__(self):
        self.pl = []        #保存系统中的所有进程
        self.result = []    #保存系统的中的杀毒程序
    # 获取系统中exe程序
    def search(self):
        self.pl = re.findall('.*?\.exe', tasklist)


    # 获取的系统中存在哪些杀毒程序
    def get(self):
        for i in self.pl:
            d = {}
            if (i in ALLEXE):
                d[i] = ALLEXE[i]
                self.result.append(d)
a = SP()
a.search()
a.get()
print(a.result)
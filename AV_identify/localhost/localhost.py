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
        self.pl = []        #����ϵͳ�е����н���
        self.result = []    #����ϵͳ���е�ɱ������
    # ��ȡϵͳ��exe����
    def search(self):
        self.pl = re.findall('.*?\.exe', tasklist)


    # ��ȡ��ϵͳ�д�����Щɱ������
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
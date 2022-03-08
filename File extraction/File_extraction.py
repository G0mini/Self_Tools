import os
import time
import threading
from shutil import copyfile

start=time.time()
filepaths=[]
key=input("请输入Key:") #提取文件中的关键字
Xpath=input("请输入保存文件夹路径:") #提取文件保存位置
def path(dir): # 获取路径下所有文件
    for root ,dirs ,files in os.walk(dir):
        for file in files:
            files_path=os.path.join(root ,file)
            filepaths.append(files_path)

def read(): #读取所有文件，判断是否存在key，Copy
    for filepath in filepaths:
        if filepath[-3:]=='php':
            flag = False  #初始化标签 判断字符串未在文件中
            a=open(filepath,'r',encoding='ISO-8859-1') ##解决编码问题
            b=a.readlines()
            for c in b:
                if "%s"%key in c: #判断是否存在key，存在就break
                    flag= True
                    break
            if flag == False: # 字符串未在文中，进行copy操作
                print(filepath)
                Xinpath = Xpath + "\\" + os.path.basename(filepath)
                copyfile(filepath, Xinpath)

if __name__ == '__main__':
    a=input("请输入检测文件绝对路径:") #输入要检测的cms路径
    t1=threading.Thread(target=path,args=(a,))
    t1.start()
    t1.join()
    t2=threading.Thread(target=read)
    t2.start()

end=time.time()
print ("time:%s"%(end-start))
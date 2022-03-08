import os
import threading
import datetime
filepaths=[]
dir = input("请输入根目录路径:")
redir = input("请输入url路径:")
start = datetime.datetime.now()
def path(dir):
    for root,dirs,files in os.walk(dir):
        for file in files:
            files_path=os.path.join(root,file)
            filepaths.append(files_path)
        # for dir in dirs:
        #     dir_path=os.path.join(root,dir)
        #     path(dir_path)
t2=threading.Thread(target=path,args=(dir,))
t2.start()

def result():
    for x in filepaths:
         if x[-3:]!="jpg" and x[-3:]!="png" and x[-3:]!="gif" and x[-3:]!="ico" and x[-3:]!="css" and x[-3:]!="woff" and x[-3:]!="eot" and x[-3:]!="svg" and x[-3:]!="ttf" and x[-4:]!="woff" and x[-5:]!="woff2" and x[-3:]!="map" and x[-3:]!="mp4" and x[-3:]!="dat" and x[-3:]!="css":
             with open('tes.txt','a+',encoding='utf-8') as f:
                 urlpath=x.replace(dir,redir)
                 urlpath1=urlpath.replace("\\","/")
                 f.writelines(urlpath1+'\n')
         else:
            pass

t1=threading.Thread(target=result)
t1.start()

# if __name__ == "__main__":
#     t1=threading.Thread(target=path,args=(dir,)) #多线程
#     t2=threading.Thread(target=result1)
#     t1.start()
#     t2.start()
#     end=datetime.datetime.now()
#     print ("time1: %s"%(end-start))



import re
from os.path import join
import os
import time
targetDir = r"D:\pypath\zhengze\hugo-demo"
filedict = {}

def subFun(match) :
     src = match.group(0)
     src1path = f"{match.group(1)}"
     #文本中的/替换为\
     src1path = src1path.replace("/","\\")
     for k,v in filedict.items():
         if src1path in v :
             with open(v,"r",encoding="utf-8") as f :
                 content = f.read()
                 dest = content
     return dest

for(dirpath,dirnames,filenames) in os.walk(targetDir) :
    for fn in filenames :
        filepath = join(dirpath,fn)
        filedict[fn] = filepath

inc_initial = r"D:\pypath\zhengze\hugo-demo\inc_initial"
#文件：记录inc文件初始的记修改时间
def write_initial_file ():
    with open(inc_initial,"w",encoding="utf-8") as f :
        inc_initial_cont = ""
        for k, v in filedict.items():
            if "inc.md" in k :
                mtime = os.stat(v).st_mtime
                inc_initial_cont += v + " " + "|"+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(mtime))+"\n"
        f.write(inc_initial_cont)
#如果初始时间戳文件不存在，则生成该文件
if not os.path.exists(inc_initial) :
    write_initial_file()
def write_agfile(file_name):
    for k, v in filedict.items():
        if file_name in k:
            # 读取inc的修改
            with open(v, "r", encoding="utf-8") as f:
                content = f.read()
            keyword = '<jcy-include>.*"(.*)"'
            agcontent = re.sub(f"{keyword}", subFun, content)
            #写ag文件
            agfile = v.replace("inc", "ag")
            with open(agfile, "w", encoding="utf-8") as f:
                f.write(agcontent)

#读取inc记录的修改时间文件
with open(inc_initial,"r",encoding="utf-8") as f :
    mtime_content = f.read()
# 遍历inc文件及其ag文件
for k, v in filedict.items():
    if "inc.md" in k :
        # 判断ag文件是否存在
        agfile = v.replace("inc", "ag")
        if os.path.exists(agfile):
            new_k = k.replace(".","\.")
            keyword = rf"{new_k}+.\|(.+)"
            intial_compare_word = (re.findall(keyword,mtime_content))[0]
            get_mtime_temp = os.stat(v).st_mtime
            compare_word = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(get_mtime_temp))
            if compare_word == intial_compare_word :
                continue
            else:
                write_agfile(k)
                write_initial_file()
                continue
        write_agfile(k)

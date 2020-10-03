import re
from os.path import join
import os
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
for k,v in filedict.items() :
    if "inc.md" in k :
        with open(v,"r",encoding="utf-8") as f :
            content = f.read()
        keyword = '<jcy-include>.*"(.*)"'
        agcontent = re.sub(f"{keyword}",subFun,content)
        #判断ag文件是否存在
        agfile = v.replace("inc","ag")
        if os.path.exists(agfile) :
            with open(agfile,"r",encoding="utf-8") as f :
                content = f.read()
                if content == agcontent :
                    continue
        #         else:
        #             with open(agfile, "w", encoding="utf-8") as f:
        #                 f.write(agcontent)
        # else:
        with open(agfile,"w",encoding="utf-8") as f :
            f.write(agcontent)

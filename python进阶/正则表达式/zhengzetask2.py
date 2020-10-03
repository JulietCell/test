import os
import re
from os.path import join
targetDir = r"D:\pypath\zhengze\prac_re"
def subFun(match) :
    src = match.group(0)
    src1 = match.group(1)
    number = int(match.group(2)) +3
    dest = f"{src1}{number}"
    print(f"{src} 替换为 {dest}")
    return dest
for (dirpath,dirnames,filenames) in os.walk(targetDir):
    for fn in filenames:
        filepath = join(dirpath,fn)
        with open(filepath,"r",encoding="utf-8") as f :
            content = f.read()
            keyword = r"(https:\/\/www\.bilibili\.com\/video\/av74106411\/\?p=)(\d*)"
            newcontent =re.sub(f"{keyword}",subFun,content)
            with open(filepath,"w",encoding="utf-8") as f :
                f.write(newcontent)


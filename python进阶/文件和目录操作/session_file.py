import os
from os.path import join
targetDir = "D:\\pypath\\prac_re"
for (dirpath,dirnames,filenames) in os.walk(targetDir):
    for fn in filenames :
        filepath = join(dirpath,fn)
        with open(filepath,'r',encoding="utf-8") as f :
            filecontent = f.read()
            newfilecontent = filecontent
            key_word = 'https://www.bilibili.com/video/av74106411/?p='
            if key_word in filecontent :
                print(f"此文件{fn}包含内容")
                t=0
                while True:
                    pos = filecontent.find(key_word, t)
                    starNum = pos + len(key_word)
                    endNum = starNum
                    if pos == -1 :
                        break
                    while True:
                        endNum +=1
                        if not filecontent[starNum:endNum].isdigit():
                            break
                    message = filecontent[starNum:endNum-1]
                    num = int(filecontent[starNum:endNum-1]) + 3
                    newfilecontent = newfilecontent.replace(filecontent[starNum:endNum-1],str(num))
                    t = endNum +1 #预留一位，防止进位
                with open(filepath,'w',encoding="utf-8") as f :
                    f.write(newfilecontent)





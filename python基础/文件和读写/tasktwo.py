file1 = "gbk编码.txt"
file2 = "utf8编码.txt"
new_cont = ""
with open(file1) as f :
    new_cont = f.read()+"\n"

with open(file2,encoding="utf-8") as f :
    new_cont += f.read()

print(new_cont)

new_file_name = input("请输入一个文件名(最好加上.txt扩展名)：")
with open(new_file_name,"w",encoding="utf-8") as f :
    f.write(new_cont)

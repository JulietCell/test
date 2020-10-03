keyword = 'https://www.bilibili.com/video/av74106411/?p='

inputnum = 3

with open('prac_filerw.txt', encoding='utf8') as f:
    lines = f.readlines()

# 新文件的内容
newContent = ''
# 一行行分析
for line in lines:
    pos1 = line.find(keyword)
    # 没有包含关键字
    if pos1 < 0:
        newContent += line
    else:
        # 计算出数字部分的起止 下标
        startPos = pos1 + len(keyword)
        endPos = startPos
        while True:
            endPos += 1
            if not line[startPos:endPos].isdigit():
                break

        num = int(line[startPos:endPos-1]) + 3
        print(num)

        newContent += line[:startPos] + str(num) + line[endPos:]

with open('prac_filerw.txt', "w", encoding='utf8') as f:
        f.write(newContent)
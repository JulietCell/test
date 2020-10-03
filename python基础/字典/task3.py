def putInfoToDict(fileName):
    with open(fileName,"r",encoding="utf-8") as f :
        messageinfo = {}
        while True :
            line = f.readline()
            if len(line) == 0 :
                break
            if not line :
                continue
            line =line.strip().replace("('","").replace("'","").replace("),","")
            lineList = line.split(",")
            checkintime = lineList[0]
            lessonid = lineList[1].strip()
            studentid = lineList[2].strip()
            addmessage = {"lessonid":lessonid, "checkintime":checkintime}
            if studentid not in messageinfo :
                messageinfo[studentid] = []
            messageinfo[studentid].append(addmessage)
    return messageinfo

message = putInfoToDict("D:\\pypath\\0005_1.txt")

import pprint
pprint.pprint(message)


import os
from os.path import join
targetDir = 'callOthers'
for(dirpath,dirnames,filenames) in os.walk(targetDir):
    for fn in filenames:
        filepath = join(dirpath,fn)
        cmd = rf'D:\pypath\ffmpeg.exe -i "{filepath}" -af asetrate=44100*8.9/10,atempo=10/8.9 -c:v copy "{filepath}"out.mp4'
        os.system(cmd)

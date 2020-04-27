# -*- coding: utf-8 -*-
import os

LrcPath = r'C:\Users\Fuwenyue\Desktop\1'
JsonPath = r'C:\Users\Fuwenyue\Desktop\AoiTeshima\musicLrc'
FileNames = os.listdir(LrcPath) 
for FileName in FileNames:
    data = {}
    TXT = open(LrcPath + '\\' + FileName,encoding = 'utf-8')
    TXT = TXT.read()
    JsonFileName =  JsonPath + '\\' + FileName.replace('lrc','json')
    data['lrc']=TXT
    data=str(data).replace('\'','\"')
    with open(JsonFileName,'w',encoding = 'utf-8') as f:
        f.write(data)

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:43:27 2020

@author: Fuwenyue
"""

import os,random,json


BasePath = r'D:\Music'
PicLink = 'https://fuwenyue.gitee.io/'
def Main():
    DataList = []
    for root, dirs, files in os.walk(BasePath):
        for file in files:
            if 'mp3' in file:
                F = file.replace('.mp3','')
                try:
                    Song,Singer = F.split('-') # 歌曲，歌手
                except:
                    Song,Singer =['Song','Singer'] 
                Data = {"type": "","link": "","songid": "","title": "","author": "","url": "","pic": "","path": ""}
                FileName = random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',random.randint(11,12)) #从里边随机取2-7个元素
                FileName = ''.join(FileName)
                fileff = file.replace('.mp3','')
                os.rename(root + '\\' + fileff + '.mp3',root + '\\' + FileName + '.mp3')
                try:
                    os.rename(root + '\\' + fileff + '.lrc',root + '\\' + FileName + '.lrc')
                except:
                    pass
                try:
                    os.rename(root + '\\' + fileff + '.jpg',root + '\\' + FileName + '.jpg')
                except:
                    pass
                Data['songid'] = FileName
                Data['title'] = Song
                Data['author'] = Singer
                Data['path'] = root.split('\\')[-1] + '/' + FileName + '.mp3'
                Data['pic'] = PicLink +root.split('\\')[-1] +'/' +FileName + '.jpg'
                DataJson = json.dumps(Data,ensure_ascii=False)
                DataList.append(DataJson)
    st = str(DataList).replace('\'','')
    with open('musicList.json','w',encoding='utf-8') as f :
        f.write(st)

def Lrc2Json(): 
    LrcJsonPath = r'C:\Users\Fuwenyue\Desktop\lrc'
    for root, dirs, files in os.walk(BasePath):
        for file in files:
            if 'lrc' in file:
                data = {}
                TXT = open(root+'\\'+file,encoding = 'utf-8')
                TXT = TXT.read()
                TXT = TXT.replace('\'','') #删除歌词单引号
                JsonFileName =  LrcJsonPath + '\\' + file.replace('lrc','json')
                data['lrc']=TXT
                data=str(data).replace('\'','\"')
                with open(JsonFileName,'w',encoding = 'utf-8') as f:
                    f.write(data)

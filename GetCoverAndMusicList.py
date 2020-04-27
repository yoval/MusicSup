# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 07:40:31 2020

@author: Fuwenyue
"""

import os,json
from mutagen import File
from mutagen.id3 import ID3

BasePath = 'D:\\Music\\' # 音乐文件夹,需\\转义
ImgLink = 'http://cos.bizha.top/Mp3Cover/' # 图片文件夹网络链接，结尾为'/'
CosPath = 'mp3' # 音频对象储存文件夹
Mp3Names = os.listdir(BasePath) # 文件夹包含文件 
DataList = []
Count=1
def DeleY(st):
    st = st.replace('"','')
    st = st.replace('\'','')
    return st
for Mp3Name in Mp3Names:
    if 'mp3' not in Mp3Name:
        continue
    Data = {"type": "","link": "","songid": "","title": "","author": "","url": "","pic": "","path": ""}
    Mp3FilePath = BasePath + Mp3Name # Mp3文件路径
    CoverName = Mp3Name.replace('mp3','jpg')
    PicFilePath = BasePath + CoverName
    Audio = File(Mp3FilePath)
    audio = ID3(Mp3FilePath)
    audio.update_to_v23()
    Title = Audio.tags["TIT2"].text[0] # 标题
    Title = DeleY(Title)
    Singer = Audio.tags['TPE1'].text[0] # 歌手
    Singer = DeleY(Singer)
    ImgUrl = ImgLink + CoverName # 图片网络链接
    try:
        PicData = Audio.tags['APIC:cover.jpg'].data 
        with open(PicFilePath, 'wb') as img:
            img.write(PicData) 
    except:
        pass
    Data['pic'] = ImgUrl
    Data['title'] = Title
    Data['author'] = Singer
    Data['path'] = CosPath+ '/' + Mp3Name
    Data['songid'] = Count
    DataJson = json.dumps(Data,ensure_ascii=False)
    Count+=1
    DataList.append(DataJson)
    st = str(DataList).replace('\'','')
with open('musicList.json','w',encoding='utf-8') as f :
    f.write(st)




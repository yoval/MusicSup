# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os,random

OldPath = r'C:\Users\Fuwenyue\Desktop\1\3' #源音频文件夹
NewPath = r'C:\Users\Fuwenyue\Desktop\1\2' #目的音频文件夹
AllFileNames = os.listdir(OldPath) 
for Name in AllFileNames :
    FileName = random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',random.randint(11,12)) #从里边随机取2-7个元素
    FileName = ''.join(FileName)
    Dot = Name.split('.')[1]
    os.rename(OldPath + '\\' + Name,NewPath + '\\' + FileName + '.' + Dot)

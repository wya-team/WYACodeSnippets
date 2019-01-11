#!/usr/bin/env python
# coding: UTF-8

import os
import shutil
import string

path_wya_codesnippets = os.getcwd()  # 获取源文件地址(不要随意改动)
print("%s"%path_wya_codesnippets)
filelist = os.listdir(path_wya_codesnippets)
print (filelist)
path2 = path_wya_codesnippets.replace('WYACodeSnippets','')   # 需要复制到的文件夹，不要随意改动

print("%s"%path2)

for files in filelist:
    filename1 = os.path.splitext(files)[1]  # 读取文件后缀名
    filename0 = os.path.splitext(files)[0]  # 读取文件名
    print(filename1)
    m = filename1 == '.codesnippet'
    print(m)
    if m:
        full_path = os.path.join(path_wya_codesnippets, files)
        despath = path2 + filename0 + '.codesnippet'  # 为你的文件类型，即后缀名,不要随意改动
        shutil.copy(full_path, despath)

    else:
        continue

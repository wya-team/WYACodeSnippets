#!/usr/bin/env python
# coding: UTF-8

import os
import shutil
import string

path_wya_codesnippets = os.getcwd()  # 获取源文件地址(不要随意改动)
print("%s"%path_wya_codesnippets)
path2 = path_wya_codesnippets.replace('WYACodeSnippets','')   # 需要复制到的文件夹，不要随意改动
print("%s"%path2)
# 获取路径下的所有存放代码块的.codesnippets文件夹
path_block = path_wya_codesnippets + "/Block"
path_function = path_wya_codesnippets + "/Function"
path_nsobject = path_wya_codesnippets + "/NSObject"
path_other = path_wya_codesnippets + "/Other"
path_collectionview = path_wya_codesnippets + "/UICollectionView"
path_tableview = path_wya_codesnippets + "/UITableView"
path_view = path_wya_codesnippets + "/UIView"
path_viewcontroller = path_wya_codesnippets + "/UIViewController"
path_ockit = path_wya_codesnippets + "/WYAOCKit"
# 获取文件夹下的所有文件
filelist1 = os.listdir(path_block)
filelist2 = os.listdir(path_function)
filelist3 = os.listdir(path_nsobject)
filelist4 = os.listdir(path_other)
filelist5 = os.listdir(path_collectionview)
filelist6 = os.listdir(path_tableview)
filelist7 = os.listdir(path_view)
filelist8 = os.listdir(path_viewcontroller)
filelist9 = os.listdir(path_ockit)

# Block
for files in filelist1:
    filename1 = os.path.splitext(files)[1]  # 读取文件后缀名
    filename0 = os.path.splitext(files)[0]  # 读取文件名
    print(filename1)
    m = filename1 == '.codesnippet'
    print(m)
    if m:
        full_path = os.path.join(path_block, files)
        despath = path2 + filename0 + '.codesnippet'  # 为你的文件类型，即后缀名,不要随意改动
        shutil.copy(full_path, despath)

    else:
        continue
# Function
for files in filelist2:
    filename1 = os.path.splitext(files)[1]  # 读取文件后缀名
    filename0 = os.path.splitext(files)[0]  # 读取文件名
    print(filename1)
    m = filename1 == '.codesnippet'
    print(m)
    if m:
        full_path = os.path.join(path_function, files)
        despath = path2 + filename0 + '.codesnippet'  # 为你的文件类型，即后缀名,不要随意改动
        shutil.copy(full_path, despath)

    else:
        continue
# NSObject
for files in filelist3:
    filename1 = os.path.splitext(files)[1]  # 读取文件后缀名
    filename0 = os.path.splitext(files)[0]  # 读取文件名
    print(filename1)
    m = filename1 == '.codesnippet'
    print(m)
    if m:
        full_path = os.path.join(path_nsobject, files)
        despath = path2 + filename0 + '.codesnippet'  # 为你的文件类型，即后缀名,不要随意改动
        shutil.copy(full_path, despath)

    else:
        continue

# Other
for files in filelist4:
    filename1 = os.path.splitext(files)[1]  # 读取文件后缀名
    filename0 = os.path.splitext(files)[0]  # 读取文件名
    print(filename1)
    m = filename1 == '.codesnippet'
    print(m)
    if m:
        full_path = os.path.join(path_other, files)
        despath = path2 + filename0 + '.codesnippet'  # 为你的文件类型，即后缀名,不要随意改动
        shutil.copy(full_path, despath)

    else:
        continue

# UICollectionView
for files in filelist5:
    filename1 = os.path.splitext(files)[1]  # 读取文件后缀名
    filename0 = os.path.splitext(files)[0]  # 读取文件名
    print(filename1)
    m = filename1 == '.codesnippet'
    print(m)
    if m:
        full_path = os.path.join(path_collectionview, files)
        despath = path2 + filename0 + '.codesnippet'  # 为你的文件类型，即后缀名,不要随意改动
        shutil.copy(full_path, despath)

    else:
        continue

# UITableView
for files in filelist6:
    filename1 = os.path.splitext(files)[1]  # 读取文件后缀名
    filename0 = os.path.splitext(files)[0]  # 读取文件名
    print(filename1)
    m = filename1 == '.codesnippet'
    print(m)
    if m:
        full_path = os.path.join(path_tableview, files)
        despath = path2 + filename0 + '.codesnippet'  # 为你的文件类型，即后缀名,不要随意改动
        shutil.copy(full_path, despath)

    else:
        continue

# UIView
for files in filelist7:
    filename1 = os.path.splitext(files)[1]  # 读取文件后缀名
    filename0 = os.path.splitext(files)[0]  # 读取文件名
    print(filename1)
    m = filename1 == '.codesnippet'
    print(m)
    if m:
        full_path = os.path.join(path_view, files)
        despath = path2 + filename0 + '.codesnippet'  # 为你的文件类型，即后缀名,不要随意改动
        shutil.copy(full_path, despath)

    else:
        continue

# UIVIewController
for files in filelist8:
    filename1 = os.path.splitext(files)[1]  # 读取文件后缀名
    filename0 = os.path.splitext(files)[0]  # 读取文件名
    print(filename1)
    m = filename1 == '.codesnippet'
    print(m)
    if m:
        full_path = os.path.join(path_viewcontroller, files)
        despath = path2 + filename0 + '.codesnippet'  # 为你的文件类型，即后缀名,不要随意改动
        shutil.copy(full_path, despath)

    else:
        continue

# WYAOCKit
for files in filelist9:
    filename1 = os.path.splitext(files)[1]  # 读取文件后缀名
    filename0 = os.path.splitext(files)[0]  # 读取文件名
    print(filename1)
    m = filename1 == '.codesnippet'
    print(m)
    if m:
        full_path = os.path.join(path_ockit, files)
        despath = path2 + filename0 + '.codesnippet'  # 为你的文件类型，即后缀名,不要随意改动
        shutil.copy(full_path, despath)

    else:
        continue

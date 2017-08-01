# -*- coding:utf-8 -*-

import os
import random

__author__ = 'lbin'

'''
设置trainval和test数据集包含的图片
'''

# ImageSets文件夹
_IMAGE_SETS_PATH = './VOC2007/ImageSets'
_MAin_PATH = './VOC2007/ImageSets/Main'
_XML_FILE_PATH = './VOC2007/Annotations'


# Train数据集编号
_TRAIN_RATE = 0.5

if __name__ == '__main__':

    # 创建ImageSets数据集
    if os.path.exists(_IMAGE_SETS_PATH):
        print('ImageSets dir is already exists')
        if os.path.exists(_MAin_PATH):
            print('Main dir is already in ImageSets')
    else:
        os.mkdir(_IMAGE_SETS_PATH)
        os.mkdir(_MAin_PATH)

    f_test = open(os.path.join(_MAin_PATH, 'test.txt'), 'w')
    f_train = open(os.path.join(_MAin_PATH, 'trainval.txt'), 'w')
    xmlname = os.listdir(_XML_FILE_PATH)
    random.shuffle(xmlname)
    # 遍历XML文件夹
    i = 0
    #for root, dirs, files in os.walk(_XML_FILE_PATH):
    for f in xmlname:
        if i > (_TRAIN_RATE*len(xmlname) - 1):
            f_test.write(f.split('.')[0] + '\n')
        else:
            f_train.write(f.split('.')[0] + '\n')

        i += 1

    f_test.close()
    f_train.close()
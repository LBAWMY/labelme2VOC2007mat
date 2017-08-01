#coding=utf-8
import os
import shutil

#打开xml文档
xmlfiles = os.listdir('./source/xmlfiles')
numofxml = xmlfiles.__len__()
for xmlfile in xmlfiles:
    #索引目录下的xml文件
    xmlfilepath = './source/xmlfiles/' + xmlfile

    # 针对性的生成一个TXT文件
    #txtfilepath = xmlfilepath.replace('xmlfiles','transfertxtfiles','xml','txt')
    imagefilepath = xmlfilepath.replace('xmlfiles', 'imagefiles')
    imagefilepath = imagefilepath.replace('xml', 'jpg')
    destinationpath = './VOC2007/JPEGImages/'
    imagefilename = xmlfile.replace('xml', 'jpg')
    shutil.copy(imagefilepath, destinationpath)

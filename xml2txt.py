#coding=utf-8
import os
import xml.dom.minidom

#打开xml文档
xmlfiles = os.listdir('./source/xmlfiles')
numofxml = xmlfiles.__len__()
for xmlfile in xmlfiles:
    #索引目录下的xml文件
    xmlfilepath = './source/xmlfiles/' + xmlfile
    dom = xml.dom.minidom.parse(xmlfilepath)

    # 针对性的生成一个TXT文件
    #txtfilepath = xmlfilepath.replace('xmlfiles','transfertxtfiles','xml','txt')
    txtfilepath = xmlfilepath.replace('xmlfiles', 'transfertxtfiles')
    txtfilepath = txtfilepath.replace('xml', 'txt')
    txtfilename = xmlfile.replace('xml', 'txt')
    txtfile = open(txtfilepath, 'w')

    #得到xml中样本名
    root = dom.documentElement
    root
    node_filename = dom.getElementsByTagName('filename')
    pic_name = node_filename[0].firstChild.data

    txtfile.writelines(pic_name+'\n')

    #得到xml中folder名
    node_folder = dom.getElementsByTagName('folder')
    folder_name = node_folder[0].firstChild.data
    txtfile.writelines(folder_name+'\n')

    #得到图片尺寸
    node_imagesize = dom.getElementsByTagName('imagesize')
    nrows = node_imagesize[0].getElementsByTagName('nrows')[0].firstChild.data
    ncols = node_imagesize[0].getElementsByTagName('ncols')[0].firstChild.data
    txtfile.writelines(nrows+' '+ncols+'\n')

    #得到xml中各个object中的详细参数，如标签、多边形的点
    object_node = dom.getElementsByTagName('object')
    for ob in object_node:
        #标签名获取
        label = ob.getElementsByTagName('name')[0].firstChild.data
        #提示输入符号
        txtfile.writelines('label' + '\n')
        #写入标签
        txtfile.writelines(label+'\n')
        #对应的多边形顶点
        node_polygon = ob.getElementsByTagName('polygon')
        node_pt = node_polygon[0].getElementsByTagName('pt')
        numofpt = node_pt.length
        txtfile.writelines(str(numofpt) + '\n')
        for pt in node_pt:
            cor_x = pt.getElementsByTagName('x')[0].firstChild.data
            cor_y = pt.getElementsByTagName('y')[0].firstChild.data
            txtfile.writelines(cor_x + ' ' + cor_y + '\n')
    txtfile.writelines('The_end'+ '\n')
    txtfile.close()


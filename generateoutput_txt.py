import os
import numpy as np

def find_all_index(arr,item):
    return [i for i,a in enumerate(arr) if a==item]

#打开txt文档
txtfiles = os.listdir('./source/transfertxtfiles')
numoftxt = txtfiles.__len__()

#输出文件
fout = open('output.txt', 'w')
for txtfile in txtfiles:
    txtfilepath = './source/transfertxtfiles/' + txtfile
    f = open(txtfilepath, 'r')
    #得到图片名与文件名
    #picture_name = f.readline().split('\n')[0]
    #folder_name = f.readline().split('\n')[0]
    picture_name = f.readline().strip("\n")
    folder_name = f.readline().strip("\n")
    #得到图片尺寸
    imagesize = f.readline().strip("\n")
    nrows = imagesize.split(' ')[0]
    ncols = imagesize.split(' ')[0]

    #循环依次得到label相关信息
    list = f.readlines()
    labels_index = find_all_index(list, 'label\n')
    for label_index in labels_index:
        labelname = list[label_index + 1].strip("\n")
        nextsc = int(list[label_index + 2].strip("\n"))
        boxsize = []
        for i in range(nextsc):
            coach = list[label_index + 3 + i].strip("\n")
            coach = coach.split(' ')
            coach_b = []
            for tmp in coach:
                coach_b.append(int(tmp))
            boxsize.append(coach_b)
        #进行提取xmin,ymin,xmax,ymax
        #
        array_boxsize = np.array(boxsize)
        corxy_min = array_boxsize.min(0)
        corxy_max = array_boxsize.max(0)
        #再写入到txt中，写完一个就换行！在for循环内
        fout.writelines(picture_name + ' ' + labelname+ ' ' + nrows + ' ' + ncols + ' ' +
                        str(corxy_min[0]) + ' ' + str(corxy_min[1]) + ' ' +
                        str(corxy_max[0]) + ' ' + str(corxy_max[1]) + '\n')

    f.close()
fout.close()

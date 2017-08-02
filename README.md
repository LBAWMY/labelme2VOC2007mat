1、xml2txt.py
实现将labelme得到的XML文件，提取出重要信息
按顺序：***.jpg foldername imagesize label(以后仅当提示用) labelname1 numberofpoints corofpoints labelname2 ......
每一个XML都将生成一个txt文件储存在source/transfertxtfiles中

2、generateoutput_txt.py
将上述生成的txt文件依次索引，提取VOC2007中需要的xmin,ymin,xmax,ymax等信息，输出到output.txt中，每个labelname一个框框，对应txt中的一行

3、optxt2voc2007xml.py
实现将上述的output.txt中的信息生成符合VOC2007格式的xml文件，并将其储存在VOC2007/Annotations下

4、makeMaintext.py
根据当前数据，设置trainval与train的比例，对此生成训练所需的四个txt文件：
trainval.txt
test.txt
train.txt
val.txt
并将其储存在VOC2007/ImageSets/Main中

5、cpsourceImage2voc.py
前提：在source/imagefiles里面放的是所有的图片，其中就有可能含有一些没有框选的图片
XML文件都是经过框选图片以后得到的
该函数实现将source/imagefiles提取出只有医生框选的图片，并将其放到VOC2007/JPEGImages


------------------------------------------------------------------------------------------------------------------


batchname.py
功能：将source/Imagefiles中的图片进行重命名为******.jpg格式
注意：(保证顺序一致！！！)
后面额外扩展照片时切记——将原先source/Imagefiles中的图片先备份再删除，再放入全新的未经批量命名的图片，再设置函数中的i的大小，让其从那个数以后命名！！！
在terminal窗口运行python batchname.py即可，新的命名图片再上传服务器
再将原先的图片融合进来，得到扩充后的图片数据集，服务器那边得到的新的xml文件再填充到source/xmlfiles
再直接运行脚本即可自动全新生成VOC2007的数据：./odxmlgeneratenxml.sh

#!/usr/bin/python3
#coding=utf-8
#Python Version Python 3.5
from xml.sax.handler import ContentHandler
from xml.sax import parse
class HeadlineHandler(ContentHandler):
    in_headline=False
    def __init__ (self):
        ContentHandler.__init__(self)
        self.data=[]
        self.file=open('info.txt','w')
        self.file.writelines('id'+'\t'+'head\n')
        self.file.close()
    def startElement(self,name,attrs):
        if name == 'list':
            self.data.append(attrs['id'])
        if name == 'head':
            self.in_headline=True
    def endElement(self,name):
        if name == 'list':
            self.file=open('info.txt','a')
            self.file.writelines(self.data[0]+'\t'+self.data[1]+'\n')
            self.file.close()
            self.data=[]
        if name == 'head':
            self.in_headline=False
    def characters(self,string):
        if self.in_headline:
            self.data.append(string)
if __name__=='__main__':
    parse('./xmlfiles/3568809_082932109.xml', HeadlineHandler())

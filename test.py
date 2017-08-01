#coding=utf-8
from xml.dom.minidom import parse,parseString
class XmlConfig:
    def __init__(self,path):
        self.xmlData=self.GetXml(path)

    def GetText(self,nodelist):
        r=""
        for nxd in nd.childNodes:
            rr=r+nxd.nodeValue
        return r
    #获取xml所有数据
    def GetXml(self,path):
        doc1=parse(path)
        st=doc1.firstChild
        websites= st.childNodes
        lstList=[]
        for sw in websites:
            if sw.nodeType==sw.ELEMENT_NODE :
                lsty=[]
                for nd in sw.childNodes:
                    if nd.nodeType==nd.ELEMENT_NODE:
                        ndName= nd.nodeName
                        ndValue= nd.firstChild.data
                        b=(ndName,ndValue)
                        lsty.append(b)
                        lstList.append(lsty)
        return lstList

    #获取单个节点及子节点值
    def GetSingle(self,siteName):
        for item in self.xmlData:
            for k,v in item:
                if v==siteName:
                    return item

    #获取单个节点及子节点值
    def GetSingleDict(self,siteName):
        lst=self.GetSingle(siteName)
        dic1={}
        if len(lst)>0:
            for item in lst:
                dic1[item[0]]=item[1]
        return dic1


if __name__=="__main__":
    f=XmlConfig('./xmlfiles/3568809_082932109.xml')
    print(f.xmlData)
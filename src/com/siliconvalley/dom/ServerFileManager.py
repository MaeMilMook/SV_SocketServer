'''
Created on 2014. 5. 10.

@author: cho
'''
from com.siliconvalley.dom.FileListReader import FileListReader

class ServerFileManager:
    '''
    fileList를 보여준다.
    '''
    
    
    
    def __init__(self):
        self.__fileListReader = FileListReader("D:\\Entertain\\PHOTO\\2013\\2013.03.24_실리콘밸리 워크샵2\\")
    
    def getFileList(self):
        return self.__fileListReader.getFileList()
    
    def bringFile(self, fileIndex):
        file = self.__fileListReader.getFile(fileIndex)
        return file
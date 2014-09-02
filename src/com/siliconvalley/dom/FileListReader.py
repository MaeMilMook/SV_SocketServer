'''
Created on 2014. 5. 10.

@author: cho
'''
from genericpath import isfile, isdir
import os, glob

class FileListReader:
    '''
    FileList를 읽는 Class
    '''

    def __init__(self, path):
        self.__path = os.path.join(path, '*')
        self.__repositoryPath = path
    
    def getFileList(self):
        
        self.__fileList = []
        
        self.__makeFileList(self.__path, self.__fileList, 1 , '')
        
        print(self.__fileList)
        
        return self.__fileList
        
        
    def __makeFileList(self, path, fileList, depth, parentDir):
        
        if os.path.isabs(path):
            
            it = iter(glob.iglob(path))
            
            for name in it:
                
                relativePath = os.path.join(parentDir, os.path.basename(name))
                
                fileInfo = {
                            'name' : relativePath
                            ,'size' : os.path.getsize(name)//1024
                            ,'depth' : depth
                            }
                
                fileList.append(fileInfo)
                
                if os.path.isdir(name):
                    self.__makeFileList(os.path.join(name, '*'), fileList, depth + 1, relativePath)
                    

        
        
        
    def getFile(self, index):
        
        fileInfo = self.__fileList[index]
        
        name = fileInfo['name']
        
        return self.__buildFileListToSend(name)
     
    ##수정필요
    ##파일 폴더 뎁스 문제
    def __buildFileListToSend(self, path):
        
        fileListToSend = []
        
        fullPath = os.path.join(self.__repositoryPath, path)
        
        if isfile(fullPath):
            file = open(fullPath, mode='rb')
            
            fileInfo = {'file' : file
                        ,'fileName' : path}
            
            fileListToSend.append(fileInfo)
            
        elif isdir(fullPath):
            
            filesUnderPath = os.path.join(fullPath, '*' )
            
            it = iter(glob.iglob(filesUnderPath))
            
            for filePath in it:
                
                if isfile(filePath) :
                
                    file = open(filePath, mode='rb')
                    
                    fileName = filePath.replace(self.__repositoryPath, '')
                    
                    fileInfo = {'file' : file
                            ,'fileName' : fileName}
                    
                    fileListToSend.append(fileInfo)
        
        return fileListToSend
        
        
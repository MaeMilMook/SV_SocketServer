'''
Created on 2014. 5. 1.

@author: cho
'''
from com.siliconvalley.view.ServerView import ServerView

class FileServerFileListView(ServerView):
    '''
    classdocs
    '''

    def __init__(self):
        pass
    
    def makeServerResponseView(self, client, model):
        fileList = model['fileList']
        self.__sendFileListWithSize(client, fileList)
    
    
    def __sendFileListWithSize(self, client, fileList):
        import os, struct
        
        print(fileList)
        
        fileNameList = []
        fileNameList.append('===Sever File List===\r\n')
        fileNameList.append('\tNumber\tFileName')
        fileNameList.append('\r\n')
        
        for idx, fileName in enumerate(fileList):
            baseName = os.path.basename(fileName)
            
            fileNameList.append('|--\t')
            fileNameList.append(str(idx))
            fileNameList.append('\t')
            fileNameList.append(baseName)
            fileNameList.append('\r\n')
        
        encodedBaseName = ''.join(fileNameList).encode('utf_8')
        
        #send data with Size, Count
        client.sendall(struct.pack('>i', len(encodedBaseName)) + struct.pack('>i', len(fileList)) + encodedBaseName)
       
        
    #Not Used
    def __sendFileListWithSep(self, client, fileList):
        import os
        
        print(fileList)
        
        fileNameList = []
        fileNameList.append('===Sever File List===\r\n')
        fileNameList.append('\tNumber\tFileName')
        fileNameList.append('\r\n')
        
        for idx, fileName in enumerate(fileList):
            baseName = os.path.basename(fileName)
            
            fileNameList.append('|--\t')
            fileNameList.append(str(idx))
            fileNameList.append('\t')
            fileNameList.append(baseName)
            fileNameList.append('\r\n')
        
        fileNames = ''.join(fileNameList)
        
        encodedBaseName = fileNames.encode('utf_8')
        
        client.sendall(encodedBaseName + 'EOF')
    

        
'''
Created on 2014. 6. 17.

@author: cho
'''
from com.siliconvalley.view.ServerView import ServerView

import os, struct

class FileSendingView(ServerView):
    '''
    classdocs
    '''

    def __init__(self):
        pass
    
    def makeServerResponseView(self, client, model):

        files = model['files']
        
        #send fileCnt
        client.sendall(struct.pack('>i', len(files)))
        
        for fileInfo in files:
            self.__sendFileToClient(client, fileInfo)
        
            
    def __sendFileToClient(self, client, fileInfo):
        
        fileName = fileInfo['fileName']
        file = fileInfo['file']
        
        #send fileName
        baseName = fileName.encode('utf-8')
        
        #send fileSize
        client.sendall(struct.pack('>i', len(baseName)) + baseName)
        
        #send fileLength
        fileLength = os.path.getsize(file.name)
        
        client.sendall(struct.pack('>i', fileLength))
        
        lines = file.readlines()
        
        for line in lines:
            client.sendall(line)
        
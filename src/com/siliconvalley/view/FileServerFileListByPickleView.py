'''
Created on 2014. 6. 13.

@author: cho
'''

from com.siliconvalley.view.ServerView import ServerView

class FileServerFileLisByPickleView(ServerView):
    '''
    classdocs
    '''
    def __init__(self):
        pass
        
        
    def makeServerResponseView(self, client, model):
        fileNameList = model['fileNameList']
        self.__sendFileListWithSize(client, fileNameList)
        
    def __sendFileListWithSize(self, client, fileNameList):
        import struct, pickle
        
        bFileNameList = pickle.dumps(fileNameList)
        
        #send data with Size, Count
        client.sendall(struct.pack('>i', len(bFileNameList)) + bFileNameList)

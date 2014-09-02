'''
Created on 2014. 5. 1.

@author: cho
'''

class FileServer:
    '''
    Server interface
    '''


    def __init__(self):
        pass
    
    def makeServerToReady(self, ip, port, listenCount):
        pass
    
    def readSelectedFileFromDir(self, filePath):
        pass
    
    def sendSelectedFileToCilent(self, client ,filePath):
        pass
    
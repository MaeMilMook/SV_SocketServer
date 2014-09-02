'''
Created on 2014. 5. 1.

@author: cho
'''
from com.siliconvalley.facade.FileServer import FileServer
import socket
import sys, struct

class SocketFileServer(FileServer):
    '''
    Socket File Server
    '''
    __sock = None

    def __init__(self):
        print('socketServer created')

    def makeServerToReady(self, ip, port, listenCount):
        
        if self.__sock is None :
                  
            self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
            print('Socket Created')
        
            try:
                self.__sock.bind((ip, port))
            except socket.error:
                print('Bind failed')
                sys.exit()
                
            print('Socket bind complete')
            
            self.__sock.listen(listenCount)
            
            print('Socket now listening')
            
            
    def acceptRequest(self):
        client, addr = self.__sock.accept()
        
        print('Connected with', addr[0], ' : ', str(addr[1]), 'client : ', client)
        
        fileNameList = self.__serverFileManager.getFileList()
        
        self.__fileServerViewListener.listenView(client, 'fileListView', {'fileNameList' : fileNameList})
        
        print('message send successfully')
        
        wantedFile = client.recv(4)
        
        wantedFile = struct.unpack('>i', wantedFile)[0]
        
        ##Log##
        print('wantedFile:', wantedFile, '\tinfo :', fileNameList[wantedFile])
        
        if wantedFile >= 0:
            files = self.__serverFileManager.bringFile(wantedFile)
        
            self.__fileServerViewListener.listenView(client, 'fileSendingView', {'files' : files})
            
            for file in files:
                file['file'].close()
            
        else:
            print('stop to send File.')
    
    def setServerFileManager(self, serverFileManager):
        self.__serverFileManager = serverFileManager
        
    def setFileServerViewListener(self, fileServerViewListener):
        self.__fileServerViewListener = fileServerViewListener
        

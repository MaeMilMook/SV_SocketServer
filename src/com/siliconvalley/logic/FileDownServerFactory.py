'''
Created on 2014. 5. 1.

@author: cho
'''
from com.siliconvalley.facade.ServerFactory import ServerFactory
from com.siliconvalley.logic.SocketFileServer import SocketFileServer


class FileDownServerFactory(ServerFactory):
    '''
    file Download Server Factory
    '''


    def __init__(self):
        pass
    
    def createServer(self, serverType):
        if serverType is ServerTypes.Socket:
            return SocketFileServer()


class ServerTypes:
    Socket = 1 
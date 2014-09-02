'''
Created on 2014. 5. 1.

@author: cho
'''
from com.siliconvalley.logic.FileDownServerFactory import FileDownServerFactory
from com.siliconvalley.logic.FileDownServerFactory import ServerTypes
from com.siliconvalley.view.FileServerFileListView import FileServerFileListView
from com.siliconvalley.viewResolve.FileServerViewResolver import FileServerViewResolver
from com.siliconvalley.viewListener.FileServerViewListener import FileServerViewListener
from com.siliconvalley.dom.ServerFileManager import ServerFileManager
from com.siliconvalley.view.FileServerFileListByPickleView import FileServerFileLisByPickleView
from com.siliconvalley.view.FileSendingView import FileSendingView

if __name__ == '__main__':
    
    ''' Configuration Start'''
    
    #FileList Console View
    #fileServerFileListView = FileServerFileListView()
    fileServerFileListView = FileServerFileLisByPickleView()
    fileSendingView = FileSendingView()
    
    
    #ViewResolver
    viewResolver = FileServerViewResolver()
    viewResolver.setView('fileListView', fileServerFileListView)
    viewResolver.setView('fileSendingView', fileSendingView)
    
    #View Listener
    fileServerViewListener = FileServerViewListener()
    fileServerViewListener.setViewResolver(viewResolver)
    
    #Factory 생성
    serverFactory = FileDownServerFactory()
    
    #소켓 서버 생성
    fileServer = serverFactory.createServer(ServerTypes.Socket)
    fileServer.setFileServerViewListener(fileServerViewListener)
    fileServer.setServerFileManager(ServerFileManager())
    
    ''' Configuration End'''
    
    #fileserver bind, listen
    fileServer.makeServerToReady('127.0.0.1', 8889, 10)
    
    while True :
        #fileserver accept
        fileServer.acceptRequest()
    
    
    
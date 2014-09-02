'''
Created on 2014. 5. 11.

@author: cho
'''
from com.siliconvalley.viewListener.ViewListner import ViewListner

class FileServerViewListener(ViewListner):
    '''
    classdocs
    '''
    
    def __init__(self):
        pass
        
    def listenView(self, client, viewName, model):
        view = self.__viewResolver.getView(viewName)
        view.makeServerResponseView(client, model)
        
    def setViewResolver(self, viewResolver):
        self.__viewResolver = viewResolver
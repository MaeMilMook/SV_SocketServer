'''
Created on 2014. 5. 10.

@author: cho
'''
from com.siliconvalley.viewResolve.ViewResolver import ViewResolver

class FileServerViewResolver(ViewResolver):
    '''
    veiw resolver 구현체
    '''

    def __init__(self):
        self.__viewDic = {}
    
    def getView(self, viewName):
        return self.__viewDic[viewName]
    
    def setView(self, viewName, view):
        self.__viewDic[viewName] = view
        
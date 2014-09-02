'''
Created on 2014. 5. 10.

@author: cho
'''
from com.siliconvalley.dom.FileListPresenter import FileListPresenter

if __name__ == '__main__':
    
    presentor = FileListPresenter()
    
    fileList = presentor.getFileList()
    
    print(fileList)
    
    nb = input('Choose a number : ')
    
    file = presentor.bringFile(int(nb))
    
    print(file)
    
    presentor.writeSelectedFile(None, file)
    

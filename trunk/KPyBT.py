#!/usr/bin/python2.4

import sys
import os
from qt import SIGNAL
from kdecore import i18n, KAboutData, KApplication, KGlobal, KIcon, KCmdLineArgs
from KPyBTMain import *

if __name__=="__main__":
    mainpath = os.path.dirname (os.path.abspath (sys.argv[0]))
    print mainpath
    authorname='Stephan Hermann'
    authormail='sh@sourcecode.de'
    prgVersion='0.1'
    lic=KAboutData.License_GPL
    prgName='KPyBT'
    prgDesc='A Python KDE BitTorrent Client'
    authordesc=i18n("Maintainer and Core Developer")
    about=KAboutData(prgName,prgName,prgVersion,prgDesc,lic,"&copy; 2005")
    about.addAuthor(authorname,str(authordesc),authormail)
    KCmdLineArgs.init(sys.argv,about)
    app=KApplication()
    mainWindow=KPyBTMainWindow(mainpath)
    mainWindow.show()
    app.setMainWidget(mainWindow)
    
    app.exec_loop()
    

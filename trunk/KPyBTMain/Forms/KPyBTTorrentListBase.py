# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KPyBTTorrentListBase.ui'
#
# Created: Mi Apr 27 00:41:45 2005
#      by: The PyQt User Interface Compiler (pyuic) 3.14.1
#
# WARNING! All changes made in this file will be lost!


import sys
from qt import *
from kdecore import KCmdLineArgs, KApplication
from kdeui import *



class KPyBTTorrentListBase(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("KPyBTTorrentListBase")


        KPyBTTorrentListBaseLayout = QGridLayout(self,1,1,11,6,"KPyBTTorrentListBaseLayout")

        self.lvTorrentList = KListView(self,"lvTorrentList")
        self.lvTorrentList.addColumn(self.__tr("No."))
        self.lvTorrentList.addColumn(self.__tr("S"))
        self.lvTorrentList.addColumn(self.__tr("Filename"))
        self.lvTorrentList.addColumn(self.__tr("DLoaded"))
        self.lvTorrentList.addColumn(self.__tr("ULoaded"))
        self.lvTorrentList.addColumn(self.__tr("DwnRate"))
        self.lvTorrentList.addColumn(self.__tr("IpRate"))
        self.lvTorrentList.addColumn(self.__tr("EstTime"))

        KPyBTTorrentListBaseLayout.addWidget(self.lvTorrentList,0,0)

        self.languageChange()

        self.resize(QSize(374,184).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)


    def languageChange(self):
        self.setCaption(self.__tr("Form2"))
        self.lvTorrentList.header().setLabel(0,self.__tr("No."))
        self.lvTorrentList.header().setLabel(1,self.__tr("S"))
        self.lvTorrentList.header().setLabel(2,self.__tr("Filename"))
        self.lvTorrentList.header().setLabel(3,self.__tr("DLoaded"))
        self.lvTorrentList.header().setLabel(4,self.__tr("ULoaded"))
        self.lvTorrentList.header().setLabel(5,self.__tr("DwnRate"))
        self.lvTorrentList.header().setLabel(6,self.__tr("IpRate"))
        self.lvTorrentList.header().setLabel(7,self.__tr("EstTime"))


    def __tr(self,s,c = None):
        return qApp.translate("KPyBTTorrentListBase",s,c)

if __name__ == "__main__":
    appname     = ""
    description = ""
    version     = ""

    KCmdLineArgs.init (sys.argv, appname, description, version)
    a = KApplication ()

    QObject.connect(a,SIGNAL("lastWindowClosed()"),a,SLOT("quit()"))
    w = KPyBTTorrentListBase()
    a.setMainWidget(w)
    w.show()
    a.exec_loop()

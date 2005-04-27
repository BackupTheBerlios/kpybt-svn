# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KPyBTTorrentBase.ui'
#
# Created: Mi Apr 27 00:41:44 2005
#      by: The PyQt User Interface Compiler (pyuic) 3.14.1
#
# WARNING! All changes made in this file will be lost!


import sys
from qt import *
from kdecore import KCmdLineArgs, KApplication
from kdeui import *



class KPyBTTorrentBase(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("KPyBTTorrentBase")


        KPyBTTorrentBaseLayout = QGridLayout(self,1,1,11,6,"KPyBTTorrentBaseLayout")

        self.tabTorrent = KTabWidget(self,"tabTorrent")
        self.tabTorrent.setCurrentPage(-1)

        KPyBTTorrentBaseLayout.addWidget(self.tabTorrent,0,0)

        self.languageChange()

        self.resize(QSize(431,270).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)


    def languageChange(self):
        self.setCaption(self.__tr("Form1"))


    def __tr(self,s,c = None):
        return qApp.translate("KPyBTTorrentBase",s,c)

if __name__ == "__main__":
    appname     = ""
    description = ""
    version     = ""

    KCmdLineArgs.init (sys.argv, appname, description, version)
    a = KApplication ()

    QObject.connect(a,SIGNAL("lastWindowClosed()"),a,SLOT("quit()"))
    w = KPyBTTorrentBase()
    a.setMainWidget(w)
    w.show()
    a.exec_loop()

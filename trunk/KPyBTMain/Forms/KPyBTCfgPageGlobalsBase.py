# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KPyBTCfgPageGlobalsBase.ui'
#
# Created: Mi Apr 27 00:41:45 2005
#      by: The PyQt User Interface Compiler (pyuic) 3.14.1
#
# WARNING! All changes made in this file will be lost!


import sys
from qt import *
from kdecore import KCmdLineArgs, KApplication
from kdeui import *



class KPyBTCfgPageGlobalsBase(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("KPyBTCfgPageGlobalsBase")


        KPyBTCfgPageGlobalsBaseLayout = QGridLayout(self,1,1,5,5,"KPyBTCfgPageGlobalsBaseLayout")

        layout6 = QVBoxLayout(None,0,5,"layout6")

        self.textLabel1 = QLabel(self,"textLabel1")
        layout6.addWidget(self.textLabel1)

        self.textLabel2 = QLabel(self,"textLabel2")
        layout6.addWidget(self.textLabel2)

        KPyBTCfgPageGlobalsBaseLayout.addLayout(layout6,0,0)

        layout7 = QVBoxLayout(None,0,0,"layout7")

        self.kcfg_TorrentDirectory = KLineEdit(self,"kcfg_TorrentDirectory")
        layout7.addWidget(self.kcfg_TorrentDirectory)

        self.kcfg_DownloadDirectory = KLineEdit(self,"kcfg_DownloadDirectory")
        layout7.addWidget(self.kcfg_DownloadDirectory)

        KPyBTCfgPageGlobalsBaseLayout.addLayout(layout7,0,1)

        layout11 = QVBoxLayout(None,0,0,"layout11")

        self.btnTorrentDir = QToolButton(self,"btnTorrentDir")
        layout11.addWidget(self.btnTorrentDir)

        self.btnDownloadDir = QToolButton(self,"btnDownloadDir")
        layout11.addWidget(self.btnDownloadDir)

        KPyBTCfgPageGlobalsBaseLayout.addLayout(layout11,0,2)

        layout4 = QGridLayout(None,1,1,0,5,"layout4")

        self.buttonGroup1 = QButtonGroup(self,"buttonGroup1")
        self.buttonGroup1.setColumnLayout(0,Qt.Vertical)
        self.buttonGroup1.layout().setSpacing(5)
        self.buttonGroup1.layout().setMargin(5)
        buttonGroup1Layout = QGridLayout(self.buttonGroup1.layout())
        buttonGroup1Layout.setAlignment(Qt.AlignTop)

        self.kcfg_TorrentStartImmediatly = QCheckBox(self.buttonGroup1,"kcfg_TorrentStartImmediatly")

        buttonGroup1Layout.addWidget(self.kcfg_TorrentStartImmediatly,0,0)

        self.kcfg_TorrentRemoveFromListAfterFinish = QCheckBox(self.buttonGroup1,"kcfg_TorrentRemoveFromListAfterFinish")

        buttonGroup1Layout.addWidget(self.kcfg_TorrentRemoveFromListAfterFinish,1,0)

        layout4.addWidget(self.buttonGroup1,1,0)

        self.buttonGroup2 = QButtonGroup(self,"buttonGroup2")
        self.buttonGroup2.setColumnLayout(0,Qt.Vertical)
        self.buttonGroup2.layout().setSpacing(5)
        self.buttonGroup2.layout().setMargin(5)
        buttonGroup2Layout = QGridLayout(self.buttonGroup2.layout())
        buttonGroup2Layout.setAlignment(Qt.AlignTop)

        self.kcfg_DeleteDatafileAfterStop = QRadioButton(self.buttonGroup2,"kcfg_DeleteDatafileAfterStop")

        buttonGroup2Layout.addWidget(self.kcfg_DeleteDatafileAfterStop,1,0)

        self.kcfg_DeleteTorrentAndDataFileAfterStop = QRadioButton(self.buttonGroup2,"kcfg_DeleteTorrentAndDataFileAfterStop")

        buttonGroup2Layout.addWidget(self.kcfg_DeleteTorrentAndDataFileAfterStop,2,0)

        self.kcfg_TorrentDeleteAfterStop = QRadioButton(self.buttonGroup2,"kcfg_TorrentDeleteAfterStop")

        buttonGroup2Layout.addWidget(self.kcfg_TorrentDeleteAfterStop,0,0)

        layout4.addWidget(self.buttonGroup2,0,0)

        KPyBTCfgPageGlobalsBaseLayout.addMultiCellLayout(layout4,1,1,0,2)

        self.languageChange()

        self.resize(QSize(464,258).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.textLabel1.setBuddy(self.kcfg_TorrentDirectory)
        self.textLabel2.setBuddy(self.kcfg_DownloadDirectory)


    def languageChange(self):
        self.setCaption(self.__tr("Form2"))
        self.textLabel1.setText(self.__tr("Torrentfile Dire&ctory:"))
        self.textLabel2.setText(self.__tr("Download Director&y:"))
        self.btnTorrentDir.setText(self.__tr("..."))
        self.btnDownloadDir.setText(self.__tr("..."))
        self.buttonGroup1.setTitle(self.__tr("Torrent Handling"))
        self.kcfg_TorrentStartImmediatly.setText(self.__tr("Start torrent &download immediatly"))
        self.kcfg_TorrentStartImmediatly.setAccel(self.__tr("Alt+D"))
        self.kcfg_TorrentRemoveFromListAfterFinish.setText(self.__tr("Remo&ve torrent from list, after the download finished"))
        self.kcfg_TorrentRemoveFromListAfterFinish.setAccel(self.__tr("Alt+V"))
        self.buttonGroup2.setTitle(self.__tr("File handling"))
        self.kcfg_DeleteDatafileAfterStop.setText(self.__tr("Delete datafile &after torrent is stopped?"))
        self.kcfg_DeleteDatafileAfterStop.setAccel(self.__tr("Alt+A"))
        self.kcfg_DeleteTorrentAndDataFileAfterStop.setText(self.__tr("Delete Torre&ntfile+Datafile after torrent is stopped?"))
        self.kcfg_DeleteTorrentAndDataFileAfterStop.setAccel(self.__tr("Alt+N"))
        self.kcfg_TorrentDeleteAfterStop.setText(self.__tr("Delete T&orrentfile after torrent is stopped?"))
        self.kcfg_TorrentDeleteAfterStop.setAccel(self.__tr("Alt+O"))


    def __tr(self,s,c = None):
        return qApp.translate("KPyBTCfgPageGlobalsBase",s,c)

if __name__ == "__main__":
    appname     = ""
    description = ""
    version     = ""

    KCmdLineArgs.init (sys.argv, appname, description, version)
    a = KApplication ()

    QObject.connect(a,SIGNAL("lastWindowClosed()"),a,SLOT("quit()"))
    w = KPyBTCfgPageGlobalsBase()
    a.setMainWidget(w)
    w.show()
    a.exec_loop()

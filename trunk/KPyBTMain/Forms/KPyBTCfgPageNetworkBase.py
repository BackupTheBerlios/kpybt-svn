# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KPyBTCfgPageNetworkBase.ui'
#
# Created: Mi Apr 27 12:21:20 2005
#      by: The PyQt User Interface Compiler (pyuic) 3.14.1
#
# WARNING! All changes made in this file will be lost!


import sys
from qt import *
from kdecore import KCmdLineArgs, KApplication
from kdeui import *



class KPyBTCfgPageNetworkBase(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("KPyBTCfgPageNetworkBase")


        KPyBTCfgPageNetworkBaseLayout = QGridLayout(self,1,1,11,6,"KPyBTCfgPageNetworkBaseLayout")

        layout6 = QGridLayout(None,1,1,0,6,"layout6")

        layout1 = QVBoxLayout(None,0,6,"layout1")

        self.textLabel1 = QLabel(self,"textLabel1")
        layout1.addWidget(self.textLabel1)

        self.textLabel1_2 = QLabel(self,"textLabel1_2")
        layout1.addWidget(self.textLabel1_2)

        self.textLabel2 = QLabel(self,"textLabel2")
        layout1.addWidget(self.textLabel2)

        layout6.addLayout(layout1,0,0)

        layout5 = QVBoxLayout(None,0,6,"layout5")

        self.kcfg_BindIP = KLineEdit(self,"kcfg_BindIP")
        layout5.addWidget(self.kcfg_BindIP)

        layout3 = QHBoxLayout(None,0,6,"layout3")
        spacer1 = QSpacerItem(41,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout3.addItem(spacer1)

        self.kcfg_HttpTimeout = KIntSpinBox(self,"kcfg_HttpTimeout")
        self.kcfg_HttpTimeout.setMaxValue(3600)
        self.kcfg_HttpTimeout.setValue(60)
        layout3.addWidget(self.kcfg_HttpTimeout)
        layout5.addLayout(layout3)

        layout4 = QHBoxLayout(None,0,6,"layout4")
        spacer2 = QSpacerItem(41,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout4.addItem(spacer2)

        self.kcfg_KeepaliveInterval = KIntSpinBox(self,"kcfg_KeepaliveInterval")
        self.kcfg_KeepaliveInterval.setMaxValue(3600)
        self.kcfg_KeepaliveInterval.setValue(120)
        layout4.addWidget(self.kcfg_KeepaliveInterval)
        layout5.addLayout(layout4)

        layout6.addLayout(layout5,0,1)

        KPyBTCfgPageNetworkBaseLayout.addLayout(layout6,0,0)

        self.languageChange()

        self.resize(QSize(282,120).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.textLabel1.setBuddy(self.kcfg_BindIP)
        self.textLabel1_2.setBuddy(self.kcfg_HttpTimeout)
        self.textLabel2.setBuddy(self.kcfg_KeepaliveInterval)


    def languageChange(self):
        self.setCaption(self.__tr("Form1"))
        self.textLabel1.setText(self.__tr("L&ocal IP:"))
        QToolTip.add(self.textLabel1,self.__tr("ip to bind to locally"))
        QWhatsThis.add(self.textLabel1,self.__tr("ip to bind to locally"))
        self.textLabel1_2.setText(self.__tr("HTTP Ti&meout:"))
        QToolTip.add(self.textLabel1_2,self.__tr("number of seconds to wait before assuming that an http connection has timed out"))
        QWhatsThis.add(self.textLabel1_2,self.__tr("number of seconds to wait before assuming that an http connection has timed out"))
        self.textLabel2.setText(self.__tr("&Keepalive Interval:"))
        QToolTip.add(self.textLabel2,self.__tr("number of seconds to pause between sending keepalives"))
        QWhatsThis.add(self.textLabel2,self.__tr("number of seconds to pause between sending keepalives"))
        self.kcfg_BindIP.setText(self.__tr("000.000.000.000"))
        self.kcfg_BindIP.setInputMask(self.__tr("###.###.###.###; "))
        QToolTip.add(self.kcfg_BindIP,self.__tr("ip to bind to locally"))
        QWhatsThis.add(self.kcfg_BindIP,self.__tr("ip to bind to locally"))
        QToolTip.add(self.kcfg_HttpTimeout,self.__tr("number of seconds to wait before assuming that an http connection has timed out"))
        QWhatsThis.add(self.kcfg_HttpTimeout,self.__tr("number of seconds to wait before assuming that an http connection has timed out"))
        QToolTip.add(self.kcfg_KeepaliveInterval,self.__tr("number of seconds to pause between sending keepalives"))
        QWhatsThis.add(self.kcfg_KeepaliveInterval,self.__tr("number of seconds to pause between sending keepalives"))


    def __tr(self,s,c = None):
        return qApp.translate("KPyBTCfgPageNetworkBase",s,c)

if __name__ == "__main__":
    appname     = ""
    description = ""
    version     = ""

    KCmdLineArgs.init (sys.argv, appname, description, version)
    a = KApplication ()

    QObject.connect(a,SIGNAL("lastWindowClosed()"),a,SLOT("quit()"))
    w = KPyBTCfgPageNetworkBase()
    a.setMainWidget(w)
    w.show()
    a.exec_loop()

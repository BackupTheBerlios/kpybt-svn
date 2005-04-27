from qt import QIconSet
from kdecore import *
from kdeui import *
from kfile import *
from KPyBTMySettings import *
from KPyBTConfigDialog import *
from KPyBTWidgets import *
import os,sys

class KPyBTMainWindow(KMainWindow):
    def __init__(self,mainpath):
        KMainWindow.__init__(self)
        print os.path.join (mainpath, "KPyBTui.rc")
        self.configDialog=None
        self.mySettings=KPyBTMySettings()
        self.mySettings.readConfig()
        self.initActions()
        self.createGUI (os.path.join (mainpath, "KPyBTui.rc"), 0)
        self.initView()
        self.initStatusBar()
    def initActions(self):
        scNull=KShortcut.null()
        acts=self.actionCollection()
        icons=KIconLoader()
        # File Menu
        self.fileOpenTorrentAction=KAction(i18n("Open Torrent..."),QIconSet(icons.loadIcon("fileopen",KIcon.Toolbar)),KStdAccel.shortcut(KStdAccel.Open),self.slotFileOpenTorrent,acts,"fileOpenTorrent")
        self.fileOpenLocationAction=KAction(i18n("Open Torrent Directory..."),QIconSet(icons.loadIcon("fileimport",KIcon.Toolbar)),scNull,self.slotFileOpenTorrentLocation,acts,"fileOpenTorrentDir")        
        self.fileExitAction=KAction(i18n("E&xit"),QIconSet(icons.loadIcon("exit",KIcon.Toolbar)),KStdAccel.shortcut(KStdAccel.Quit),self.slotFileExit,acts,"fileExit")
        # Settings Menu
        self.settingsConfigureAppAction=KAction(i18n("Configure KPyBT..."),QIconSet(icons.loadIcon("configure",KIcon.Toolbar)),scNull,self.slotSettingsConfigureApp,acts,"settingsConfigureApp")
        # Torrents Menu
        self.browseTorrents=KAction(i18n("Browse Torrents"),scNull,self.slotBrowseTorrents, self.actionCollection(),"browse_torrents")
    def initView(self):
        self.torrentTab=KPyBTTorrentWidget(self)
        self.setCentralWidget(self.torrentTab)
    def initStatusBar(self):
        self.statusBar().insertItem(i18n("Torrentcount: 0"),1000,0,0)
        self.statusBar().insertItem(i18n("AllDwn: 00.00 kb/s"),1001,0,1)
        self.statusBar().insertItem(i18n("AllUp: 00.00 kb/s"),1002,0,2)
    # file Action Slots
    def slotFileOpenTorrent(self):
        fileName=KFileDialog.getOpenFileName("","*.torrent|Torrent Files (*.torrent)",self,i18n("Open Torrent"))
        print fileName
        print "slotFileOpen"
    def slotFileOpenTorrentLocation(self):
        directoryName=KFileDialog.getExistingDirectory("",self,"Open Torrent Directory")
        print directoryName
    def slotFileExit(self):
        self.close()
    # settings action slots
    def slotSettingsConfigureApp(self):
        if self.configDialog is None:
            self.configDialog=KPyBTConfigDialog(self,"Configure KPyBT",self.mySettings)
        if self.configDialog.exec_loop():
            self.mySettings.writeConfig()
    def slotBrowseTorrents(self):
        print "slotBrowseTorrents"

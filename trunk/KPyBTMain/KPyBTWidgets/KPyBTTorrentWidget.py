from kdecore import *
from kdeui import *
from KPyBTMain.Forms import KPyBTTorrentBase
from KPyBTTorrentListWidget import *

class KPyBTTorrentWidget(KPyBTTorrentBase):
    def __init__(self,parent):
        KPyBTTorrentBase.__init__(self,parent)
        self.tabs={}
        self.initTabs()
    def initTabs(self):
        self.torrentList=KPyBTTorrentListWidget(None)
        self.addTab(self.torrentList,i18n("Torrents"))
    def addTab(self,tabItem,tabName):
        self.tabs[tabName]=tabItem
        self.tabTorrent.addTab(tabItem,tabName)
    def listTabs(self):
        for i in self.tabs:
            print i

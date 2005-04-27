from qt import *
from kdeui import *
from kdecore import *
from kfile import *
from KPyBTMain.Forms import KPyBTCfgPageGlobalsBase

class KPyBTCfgPageGlobals(KPyBTCfgPageGlobalsBase):
    def __init__(self,parent,config):
        KPyBTCfgPageGlobalsBase.__init__(self,parent)    
        self.connect(self.btnTorrentDir,SIGNAL("clicked()"),self.slotTorrentDir)
        self.connect(self.btnDownloadDir,SIGNAL("clicked()"),self.slotDownloadDir)
    def slotTorrentDir(self):
        dirName=KFileDialog.getExistingDirectory(self.kcfg_TorrentDirectory.text(),self,"Torrent Directory")
        self.kcfg_TorrentDirectory.setText(dirName)
    def slotDownloadDir(self):
        dirName=KFileDialog.getExistingDirectory(self.kcfg_DownloadDirectory.text(),self,"Torrent Directory")
        self.kcfg_DownloadDirectory.setText(dirName)

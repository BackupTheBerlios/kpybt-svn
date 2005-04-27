from kdecore import *
from kdeui import *
from KPyBTWidgets import KPyBTCfgPageGlobals, KPyBTCfgPageNetwork

class KPyBTConfigDialog(KConfigDialog):
    def __init__(self,parent,name,config):
        KConfigDialog.__init__(self,parent,name,config)
        self.addPage(KPyBTCfgPageGlobals(self,config), "Globals", "globals", "KPyBT Global Settings")
        self.addPage(KPyBTCfgPageNetwork(self,config),"Network","network","KPyBT Network Settings")

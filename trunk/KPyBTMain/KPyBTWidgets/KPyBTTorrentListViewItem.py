from qt import *
from kdecore import *
from kdeui import *

class KPyBTTorrentListViewItem(KListViewItem):
    
    def __init__(self, key, *args):
        KListViewItem.__init__(self, key,*args)
        self.max=1000
        self.ammount=1
        self.setProgress(0)
    def setMax(self,max):
        self.max=max
    def paintCell(self, painter, colour_group, column, width, alignment):
        if column==2:
            painter.save()
            widthToPaint=width*self.percent/100
            brush=QBrush(KGlobalSettings.highlightColor())
            painter.fillRect(0,0,widthToPaint,self.height(),brush)
            painter.setPen(QPen(KGlobalSettings.highlightedTextColor(),1,Qt.SolidLine))
            painter.setFont(KGlobalSettings.fixedFont())
            text="%s" % self.ammount
            text1="%s" % self.max
            center=width/2 - QFontMetrics(KGlobalSettings.fixedFont()).width(text+"/"+text1)/2
            painter.drawText(center,QFontMetrics(KGlobalSettings.fixedFont()).ascent(),text+"/"+text1)
            painter.restore()
        else:
            KListViewItem.paintCell(self,painter,colour_group,column,width,alignment)
    def setProgress(self,ammount):
        if ammount==0: 
            ammount=1;
        self.ammount=ammount
        self.percent=100*self.ammount/self.max
        self.repaint()

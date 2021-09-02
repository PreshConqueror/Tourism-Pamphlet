  #CALLING SOURCE CODE

#IMPORT FROM PYQT5
import sys 
from ass1 import * 
from PyQt5.QtWidgets import *


#PROGRAM CODE
class MyForm(QtWidgets.QDialog):
    def __init__(self, pixmap, parent=None):
        QWidget.__init__(self, parent) 
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.scene = QGraphicsScene(self)
        item=QGraphicsPixmapItem(pixmap)
        self.scene.addItem(item) 
        self.ui.graphicsView_2.setScene(self.scene)

        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    pixmap= QtGui.QPixmap()
    pixmap.load("joburg.jpg")

    myapp = MyForm(pixmap)
    myapp.show()
    sys.exit(app.exec_())

    

 

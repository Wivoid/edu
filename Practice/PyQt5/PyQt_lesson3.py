import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Denilindo')
        self.setGeometry(500, 500, 700, 650)

        label = QLabel(self)
        label.setGeometry(0, 0, 250, 350) # x, y, width, height

        pixmap = QPixmap('Practice\PyQt5\pics\man.jpeg') # In brackets is path to image
        label.setPixmap(pixmap) # connecting image with label

        label.setScaledContents(True) # Sizes image into label

        #label.setGeometry(0, 0, label.width(), label.height())  -- Example of setting the values relative to other
        #label.setGeometry(self.width() - label.width() , self.height() - label.height()  , label.width() , label.height()) -- Bottom right corner
        label.setGeometry((self.width() - label.width()) // 2, # // 2  -- division
                           (self.height() - label.height()) // 2 ,
                             label.width(), label.height()) # Right in the middle
        #DO NOT FORGET!! It's essential for centralization to be all in brackets () // 2
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
import os, sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QHBoxLayout
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont, QFontDatabase

class Clock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel("TIME 1498821",self)
        self.timer = QTimer()
        self.time = QTime()
        self.initUI()

    def initUI(self):
        self.setGeometry(800,500,1000,300)
        self.setStyleSheet('background-color: black;')
        self.time_label.setStyleSheet('color: hsl(128, 100%, 50%);'
                                      'font-size: 150px;')

        self.time_update()
        self.timer.timeout.connect(self.time_update)
        self.timer.start(10)

        hbox = QHBoxLayout()
        hbox.addWidget(self.time_label)
        self.setLayout(hbox)

        self.time_label.setAlignment(Qt.AlignCenter)




    def time_update(self):
        current_time = self.time.currentTime().toString('h:m:s:z')
        self.time_label.setText(current_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = Clock()
    clock.show()
    sys.exit(app.exec_())
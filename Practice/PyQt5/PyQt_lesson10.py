import os, sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont, QFontDatabase

font_path = os.path.join('/VScode/Python/Rabota11/edu/Practice/PyQt5/pics/DS-DIGIT.TTF')

class Clock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel("Digital Clock",self)
        self.stop_button = QPushButton("STOP", self)
        self.timer = QTimer()
        self.time = QTime()
        self.initUI()

    def initUI(self):
        self.setGeometry(800,500,1600,500)

        self.stop_button.setStyleSheet('color: green;'
                                        'text-align: center;'
                                        'font-size: 150px')
        self.setStyleSheet('background-color: black;')
        self.time_label.setStyleSheet('color: hsl(128, 100%, 50%);')
        
        font_id = QFontDatabase.addApplicationFont(font_path) # Connects font
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0] # Creates family and connects it to number in list [0]
        my_font = QFont(font_family, 150) # Setting font properties
        self.time_label.setFont(my_font) # Setting the font itself

        self.time_update()
        self.timer.timeout.connect(self.time_update)
        self.timer.start(1)

        self.stop_button.clicked.connect(self.stop_time)

        hbox = QHBoxLayout()
        hbox.addWidget(self.time_label)
        hbox.addWidget(self.stop_button)
        self.setLayout(hbox)

        self.time_label.setAlignment(Qt.AlignHCenter)


    def time_update(self):
        self.current_time = self.time.currentTime().toString('h:m:s')
        self.time_label.setText(self.current_time)

    def stop_time(self):
        if self.stop_button.text() == "STOPPED":

            self.stop_button.setText("Stop")
            self.time_update()
            self.timer.start(1)
        else:
            self.timer.stop()
            self.stop_button.setText('STOPPED')
            


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = Clock()
    clock.show()
    sys.exit(app.exec_())
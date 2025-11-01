import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                            QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import QTime, Qt, QTimer

class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stopwatch")

        self.time_label = QLabel("00:00:00.00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.restart_button = QPushButton("Restart", self)
        self.speedup_button = QPushButton("Speed Up", self)

        self.interval = 10

        self.timer = QTimer()
        self.time = QTime(0,0,0,0) #hours, minutes, seconds, milliseconds

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.time_label.setAlignment(Qt.AlignCenter)

        self.setLayout(vbox)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.restart_button)
        hbox.addWidget(self.speedup_button)


        vbox.addLayout(hbox)
        
        self.start_button.setObjectName("start_button")
        self.stop_button.setObjectName("stop_button")
        self.restart_button.setObjectName("restart_button")
        self.speedup_button.setObjectName("speedup_button")

        self.setStyleSheet("""
            QWidget{        /* CLOCK'S BG */
                    background-color: #c7eff2;
                           }
            QPushButton, QLabel{    /* SETTING GLOBAL PROPERTIES for QPushButton, QLabel */
                        padding: 30px;
                        margin: 15px;
                        border-radius: 15px;
                           }

            QPushButton{              /* SPECIFYING PROPERTIES for QPushButton*/
                    font-size: 50px;
                        }
            QLabel{                   /* SPECIFYING PROPERTIES for QLabel*/
                    font-size: 150px;
                    color: #374666;
                        }
                           
            QPushButton#start_button{              /* SPECIFYING PROPERTIES for buttons itself*/
                        border: 5px solid #ad5e5e;
                        background-color: #bd6262;
                           }
            QPushButton#stop_button{
                        border: 5px solid #94de78;
                        background-color: #afff91;
                           }
            QPushButton#restart_button{
                        border: 5px solid #a6bae3;
                           background-color: #c7d5f2;
                           }
            QPushButton#speedup_button{
                        border: 5px solid #c785cc;
                           background-color: #f19cf7;
                           }

            QPushButton#start_button:hover{              /* Adding minimal appearance to button's style*/
                        border: 5px solid #bd6868;
                        background-color: #cf7070;
                           }
            QPushButton#stop_button:hover{
                        border: 5px solid #9eed80;
                        background-color: #befca7;
                           }
            QPushButton#restart_button:hover{
                        border: 5px solid #b1c6f2;
                           background-color: #d3def5;
                           }
            QPushButton#speedup_button:hover{
                        border: 5px solid #db94e0;
                           background-color: #f7a9fc;
                           }

            QPushButton#start_button:pressed{              /* Adding minimal appearance to button's style*/
                        border: 5px solid #a65a5a;
                        background-color: #b86161;
                           }
            QPushButton#stop_button:pressed{
                        border: 5px solid #8cd470;
                        background-color: #a8de95;
                           }
            QPushButton#restart_button:pressed{
                        border: 5px solid #9eb1d9;
                           background-color: #c1cade;
                           }
            QPushButton#speedup_button:pressed{
                        border: 5px solid #c283c7;
                           background-color: #de96e3;
                           }

        """)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.restart_button.clicked.connect(self.restart)
        self.timer.timeout.connect(self.update_display)
        self.speedup_button.clicked.connect(self.speed_up)

    def start(self):
        if self.timer.isActive():
            self.timer.stop()
            self.start_button.setText("Resume")
            self.stop_button.setText("Paused")
        else:
            self.timer.start(self.interval)
            self.start_button.setText("Stop")
            self.stop_button.setText("Stop")
            self.restart_button.setText("Restart")
            


    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def stop(self):
        self.timer.stop()
        self.stop_button.setText("Paused")

    def restart(self):
        self.timer.stop()
        self.start_button.setText("Start")
        self.stop_button.setText("Stop")
        self.restart_button.setText("Restarted")
        self.time = QTime(0,0,0,0)
        self.time_label.setText(self.format_time(self.time))

    def speed_up(self):
        if self.interval == 5:
            self.timer.stop()
            self.interval = 10
            self.speedup_button.setText("Speed Up")
        else:
            self.timer.stop()
            self.interval = self.interval // 2
            self.speedup_button.setText("x2 Speed")


    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    watch = StopWatch()
    watch.show()
    sys.exit(app.exec_())
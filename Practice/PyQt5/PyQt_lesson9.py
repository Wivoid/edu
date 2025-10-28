import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lesson 9")

        self.button1 = QPushButton("Pineapple")
        self.button2 = QPushButton("Cabbage")
        self.button3 = QPushButton("Pomegranate")
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        self.button1.setObjectName("button1") # Sets Objectname to refer to them later in stylesheets
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        # Tripple quotes uses in large stylesheets texts
        self.setStyleSheet(""" 
            QPushButton{
                font-size: 25px;
                padding: 15px 25px;""" # padding: height, width
                """margin: 40px;
                border: 2px solid;
                border-radius: 15px;
                           }
            QPushButton#button1{
                background-color: hsl(55, 96%, 73%);
            }
            QPushButton#button2{
                background-color: hsl(118, 94%, 67%);
            }
            QPushButton#button3{
                background-color: hsl(354, 55%, 51%);
            }

            QPushButton#button1:hover{
                background-color: hsl(55, 96%, 85%);
            }
            QPushButton#button2:hover{
                background-color: hsl(118, 94%, 82%);
            }
            QPushButton#button3:hover{
                background-color: hsl(354, 55%, 66%);
            }
        """)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
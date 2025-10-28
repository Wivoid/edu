import sys, keyboard
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,250,500,500)
        self.setWindowTitle('Lesson 8')

        self.textbox = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        self.label1 = QLabel("Your card:", self)
        self.label2 = QLabel("", self)
        self.initUI()


    def initUI(self):
        self.button.setGeometry(250,20,180,50)
        self.textbox.setGeometry(20, 20, 210, 50)
        self.label1.setGeometry(60,120,290,100)
        self.label2.setGeometry(90,220,250,100)

        self.button.setStyleSheet("font-size: 30px;")
        self.textbox.setStyleSheet("font-size: 25px;")
        self.label1.setStyleSheet("font-size: 60px;"
                                 "background-color: #ffec9e")
        self.label2.setStyleSheet("font-size: 25px;")

        self.textbox.setPlaceholderText("Enter your card")
        self.button.clicked.connect(self.submit)

    def submit(self):
        self.label2.setText(self.textbox.text())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
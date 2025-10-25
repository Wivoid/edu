from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,500,500)
        self.setWindowTitle("McDonald's")
        self.label = QLabel('Click on the button above', self) # Creating label
        self.initUI()


    def initUI(self):
        self.button = QPushButton('Click me', self) # Creating button
        self.button.setGeometry(150,150,200,100)  
        self.label.setGeometry(80,140,400,300)
        
        self.button.setStyleSheet('font-size: 40px;') #Appearance
        self.label.setStyleSheet('font-size: 30px;')

        self.button.clicked.connect(self.on_click) # Connecting function of a button; RULE: button.{action}.connect()



    def on_click(self): # Button function
        self.label.setText('SUUUUUUUUUUUIIIIIIIIIIIIIII')
        self.button.setDisabled(True) # Sets button disabled after being clicked



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main()
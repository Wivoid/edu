from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLabel
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300,400,500,500)
        self.setWindowTitle('Penisildo')
        self.checkbox = QCheckBox('Checked?', self)
        self.initUI()

        self.label = QLabel('No', self)    # Label for our method
        self.label.setGeometry(170, 200, 200,200)
        self.label.setStyleSheet('font-size: 120px;')


    def initUI(self): # Checkbox itself
        self.checkbox.setGeometry(95,0,500,200)
        self.checkbox.setStyleSheet('font-size: 60px;'
                                    'font-family: Arial;')
        self.checkbox.stateChanged.connect(self.checked)


    def checked(self, state):    # Method to Checkbox
        if state == Qt.Checked:      # If statement to our function
            self.label.setText('Yes') 
        else:
            self.label.setText('No')

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
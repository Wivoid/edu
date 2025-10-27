import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300,300,600,700)
        self.setWindowTitle('Lesson 7')

        self.label1 = QLabel("Say hello:", self)
        self.label2 = QLabel("Say goodbye:", self)
        self.label3 = QLabel("", self)

        self.label1.setGeometry(50,20,180,50)
        self.label2.setGeometry(50,295,245,50)
        self.label3.setGeometry(50,600,480,70)

        self.label1.setStyleSheet(
                "font-size: 40px;"
                "background-color: #edb118;")
        self.label2.setStyleSheet(
                "font-size: 40px;"
                "background-color: #edb118;")
        self.label3.setStyleSheet(
        "font-size: 50px;"
        "background-color: #50e034;")

        self.radio_button1 = QRadioButton('Hi', self) # RadioButtons
        self.radio_button2 = QRadioButton('Привіт', self)
        self.radio_button3 = QRadioButton('Привет', self)

        self.radio_button4 = QRadioButton('Bye', self)
        self.radio_button5 = QRadioButton('Прощавай', self)
        self.radio_button6 = QRadioButton('Пока', self)

        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)

        self.initUI()

    def initUI(self):

        self.radio_button1.setGeometry(40, 70, 300, 70)
        self.radio_button2.setGeometry(40, 140, 300, 70)
        self.radio_button3.setGeometry(40, 210, 300, 70)
        self.radio_button4.setGeometry(40, 350, 300, 70)
        self.radio_button5.setGeometry(40, 420, 300, 70)
        self.radio_button6.setGeometry(40, 490, 300, 70)

        self.setStyleSheet("QRadioButton{" # StyleSheet that works for all 'QRadioButton'
        "font-size: 40px;"
        "font-family: Arial;"
        "}")

        self.button_group1.addButton(self.radio_button1) # Connecting each button to their group
        self.button_group1.addButton(self.radio_button2)
        self.button_group1.addButton(self.radio_button3)
        self.button_group2.addButton(self.radio_button4)
        self.button_group2.addButton(self.radio_button5)
        self.button_group2.addButton(self.radio_button6)

        self.radio_button1.toggled.connect(self.btn_selected)
        self.radio_button2.toggled.connect(self.btn_selected)
        self.radio_button3.toggled.connect(self.btn_selected)
        self.radio_button4.toggled.connect(self.btn_selected)
        self.radio_button5.toggled.connect(self.btn_selected)
        self.radio_button6.toggled.connect(self.btn_selected)

    def btn_selected(self):
        button = self.sender()
        if button.isChecked():
                self.label3.setText(f'You said "{button.text()}"')
    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

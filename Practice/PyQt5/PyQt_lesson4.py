import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Martenuk")
        self.setGeometry(500, 350, 500, 500)
        self.initUI() # Connecting Widget to mainwindow
    
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget) # Marking Widget as a Central
 
        label1 = QLabel("Slon", self) # Labels
        label2 = QLabel("Decl", self)
        label3 = QLabel("Cup", self)
        label4 = QLabel("Water", self)
        label5 = QLabel("Wassabi", self)

        font_label = QFont('Sans', 30) # Creating font pattern
        font_label.setBold(True) # Setting it bold

        label1.setFont(font_label) # Connecting it
        label2.setFont(font_label)
        label3.setFont(font_label)
        label4.setFont(font_label)
        label5.setFont(font_label)

        label1.setStyleSheet('background-color: red;') # Some appearance
        label2.setStyleSheet('background-color: blue;')
        label3.setStyleSheet('background-color: pink;')
        label4.setStyleSheet('background-color: purple;')
        label5.setStyleSheet('background-color: aqua;')

        label1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter) # Alignment to Center
        label2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        label3.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        label4.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        label5.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        vbox = QVBoxLayout() # simplfying vbox layout

        vbox.addWidget(label1) # Adding labels to widget
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)
    
        central_widget.setLayout(vbox) # Connecting the layout of vbox to widget

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
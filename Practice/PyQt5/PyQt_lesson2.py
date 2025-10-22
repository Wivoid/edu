import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt #Qt class - is being used to alignment


class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Lesson 2')
        self.setGeometry(700, 550, 500, 500)

        label = QLabel("Hi", self)     # 1 - text; 2 - parent
        label.setFont(QFont('Sans', 20)) # Font, size
        label.setGeometry(0, 0, 500, 100) # x, y, width, height for label
        label.setStyleSheet("color: purple;"  #CSS like syntax 
        "background: #7bd1a6;" #Important! Do not forget about ; at the end
        "font-weight: bold;"
        "font-style: italic;"
        "text-decoration: underline;") 

        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # '|' combines flags; Also For absolute center: Qt.AlignCenter
        #We can also apply whether for x Qt.AlignRight / Qt.AlignLeft or for y Qt.AlignRTop / Qt.AlignBottom

def main():
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
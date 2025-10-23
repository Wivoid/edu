import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

man_path = os.path.join('/VScode/Python/Rabota11/edu/Practice/PyQt5/pics/man.jpeg') #Have some problems with image's path

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() # helps us to address to parental MainWindow
        self.setWindowTitle("Lesson 1")
        self.setGeometry(100, 300, 900, 500) # x; y width; height
        self.setWindowIcon(QIcon(man_path))


def main():
    app = QApplication(sys.argv) # Creates app manager "sys.argv" called app
    window = MainWindow()
    window.show
    sys.exit(app.exec_()) # Executes exit after closing window

if __name__ == "__main__":
    main()
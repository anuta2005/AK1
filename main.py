import sys
import random

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.a = MyWidget1()
        self.a.show()

class MyWidget1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 300)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_smile(qp)
        qp.end()

    def draw_smile(self, qp: QPainter):
        qp.setPen(QColor(255, 255, 0))
        k = random.randint(0, 50)
        qp.drawEllipse(0, 0, 10 * k, 10 * k)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
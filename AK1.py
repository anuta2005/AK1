import sys
import random
import untitled

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QtWidgets.QMainWindow, untitled.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        qp.setPen(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        k = random.randint(0, 50)
        qp.drawEllipse(0, 0, 10 * k, 10 * k)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())


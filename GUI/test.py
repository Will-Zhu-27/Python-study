from PyQt5.QtWidgets import (QWidget, QMessageBox, QApplication)
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        QMessageBox.question(self, 'ddd', 'sss')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Example()
    sys.exit(app.exec_())
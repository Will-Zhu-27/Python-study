import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog,
                             QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.show()

    def init_ui(self):
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.show_dialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')

    def show_dialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your '
                                                              'name:')

        if ok:
            self.le.setText(str(text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

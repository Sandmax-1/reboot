import sys

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi
from backend import get_skills_from_bio
from output import Ui_Form
from test import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(450, 500)
        self.setStyleSheet("QMainWindow {background: 'white';}")
        self.setupUi(self)

    def do_a_thing(self, _):
        text_from_gui = self.textEdit.toPlainText()
        skills = get_skills_from_bio(text_from_gui, 3)
        print(skills)
        self.output = Output()
        self.output.label.setText(str(skills))
        self.output.show()

    def about(self):
        QMessageBox.about(
            self,
            "About Sample Editor",
            "<p>A sample text editor app built with:</p>"
            "<p>- PyQt</p>"
            "<p>- Qt Designer</p>"
            "<p>- Python</p>",
        )


class Output(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(450, 500)
        self.setStyleSheet("QMainWindow {background: 'white';}")
        self.setupUi(self)

    def about(self):
        QMessageBox.about(
            self,
            "About Sample Editor",
            "<p>A sample text editor app built with:</p>"
            "<p>- PyQt</p>"
            "<p>- Qt Designer</p>"
            "<p>- Python</p>",
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
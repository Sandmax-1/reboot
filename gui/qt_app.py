import sys
import time
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5 import QtGui, Qt, QtCore
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
        people = ['derek', 'john', 'susan']
        for person in people:
            self.output = Output()
            self.output.textBrowser.setText(str(skills))
            self.output.label.setPixmap(QtGui.QPixmap("gui\\person.jpg"))
            name = person
            self.output.setWindowTitle(name)
            self.output.show()
            no_user_input = True
            yes_button_input = True
            while no_user_input and yes_button_input:
                QApplication.processEvents()
                time.sleep(0.05)
                no_user_input = self.output.no_button_pressed
                yes_button_input = self.output.yes_button_pressed

            if not yes_button_input:
                self.found_person=True
                print(name)
                self.output.close()
                break
            self.output.close()
        
        self.label_3.setText(f"Congratulations, you've found {name}!")
        self.label_3.adjustSize()
        # self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.move(self.label_3.x() - 100, self.label_3.y())
        self.textEdit.hide()



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
        self.no_button_pressed=True
        self.yes_button_pressed = True
        self.setFixedSize(450, 500)
        self.setStyleSheet("QMainWindow {background: 'white';}")
        self.setupUi(self)

    def no_button(self):
        self.no_button_pressed=False
    
    def yes_button(self):
        self.yes_button_pressed=False


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
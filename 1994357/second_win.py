# write a code for the second screen of app
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,QHBoxLayout, QVBoxLayout,QGroupBox, QRadioButton,QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *
from second_win import *


class MainWin(QWidget):
    def __init__(self):
        #la ventana dende esta el saludo
        super().__init__()
        #creando y configurando elementos graficos
        self.initUI()
        #establece la conexion entre los elementos
        self.connects()
        #establece la apariencia de la ventana(etiqueta, tamaño y ubicacion)
        self.set_appear()
        #inicio
        self.show()

    def nex_click(self):
        self.tw = TestWin()
        self.hide()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def ser_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

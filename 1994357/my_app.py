# write the code for main app and first screen
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
    def initUI(self):
        sefl.btn_next = QPushButton(txt next, self)
        self.hello_text = QLabel(txt hello)
        self.instruction = QLabel(txt instruction)

        self.layout_line = QVBoxLayout()
        self.layout_line.addwidget(self.hello_text, alignment = QT.AlignLeft)
        self.layout_line.addwidget(self.instruction, alignment = QT.AlignLeft)

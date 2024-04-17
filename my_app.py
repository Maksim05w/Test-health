# напиши здесь код основного приложения и первого экранаfrom PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('технические шоколадки')
main_win.move(900, 70)
main_win.resize(400, 200)
main_win.show()


v_line = QVBoxLayout()
title = QLabel('привет')
v_line.addWidget(title, alignment = Qt.AlignCenter)
main_win.setLayout(v_line)

app.exec_() 
txt_title = 'Здоровье'
win_x, win_y = 200, 100
win_width, win_height = 1000, 600
class TestWin(QWidet):
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.h_line = QLabel()
        self.r = QPushButton()
        self.l = QLineEdit(text_next)
     def __init__(self):
        super()>__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def connects(self):
        pass self.next_click



    

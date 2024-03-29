from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class Task_Widget(QWidget):
    def __init__(self, pos: int, task_string: str=''):
        super().__init__()

        self.layout = QHBoxLayout()

        left_button = QPushButton("LEFT")
        sp_retain = left_button.sizePolicy()
        sp_retain.setRetainSizeWhenHidden(True)
        left_button.setSizePolicy(sp_retain)
        left_button.clicked.connect(self.left_button_clicked)

        right_button = QPushButton("RIGHT")
        sp_retain = right_button.sizePolicy()
        sp_retain.setRetainSizeWhenHidden(True)
        right_button.setSizePolicy(sp_retain)
        right_button.clicked.connect(self.right_button_clicked)

        # Hide left/right button based on position
        if pos == 0:
            left_button.setVisible(False)
        elif pos == 2:
            right_button.setVisible(False)

        self.layout.addWidget(left_button)
        self.layout.addWidget(QLabel(task_string))
        self.layout.addWidget(right_button)
        self.setLayout(self.layout)

    def left_button_clicked(self):
        # On button clicked:
        # 1. remove widget from grandparent
        # 2. add widget to left
        # 3. If there is nothing to left, hide left button
        # 4. Show right button
        # Assumption: buttons cannot exist without there being a column to move to
        par_widget = self.layout.parentWidget()
        par_par_wid = par_widget.parentWidget()
        par_par_wid.layout().removeWidget(par_widget)
        left_par_par = par_par_wid.get_left()
        left_par_par.layout().addWidget(par_widget)
        left_button = self.layout.itemAt(0).widget()
        if left_par_par.get_left() == None:
            left_button.setVisible(False)
        else:
            left_button.setVisible(True)
        right_button = self.layout.itemAt(2).widget()
        right_button.setVisible(True)

    def right_button_clicked(self):
        # See left
        par_widget = self.layout.parentWidget()
        par_par_wid = par_widget.parentWidget()
        par_par_wid.layout().removeWidget(par_widget)
        right_par_par = par_par_wid.get_right()
        right_par_par.layout().addWidget(par_widget)
        right_button = self.layout.itemAt(2).widget()
        if right_par_par.get_right() == None:
            right_button.setVisible(False)
        else:
            right_button.setVisible(True)
        left_button = self.layout.itemAt(0).widget()
        left_button.setVisible(True)
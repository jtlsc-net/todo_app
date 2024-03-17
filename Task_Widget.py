from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class Task_Widget(QWidget):
    def __init__(self, task_string: str=''):
        super().__init__()

        self.layout = QHBoxLayout()

    def left_button_clicked(self):
        item = self.layout.itemAt(0)
        if item != None:
            widget = item.widget()
            if widget != None:
                self.layout.removeWidget(widget)
                widget.deleteLater()

    def right_button_clicked(self):
        item = self.layout.itemAt(2)
        if item != None:
            widget = item.widget()
            if widget != None:
                self.layout.removeWidget(widget)
                widget.deleteLater()

class Todo_Widget(Task_Widget):
    def __init__(self, task_string: str=''):
        super().__init__()

        right_button = QPushButton("RIGHT")
        right_button.clicked.connect(self.right_button_clicked)

        self.layout.addWidget(QLabel())
        self.layout.addWidget(QLabel(task_string))
        self.layout.addWidget(right_button)
        self.setLayout(self.layout)

class Doing_Widget(Task_Widget):
    def __init__(self, task_string: str=''):
        super().__init__()

        self.layout = QHBoxLayout()

        left_button = QPushButton("LEFT")
        left_button.clicked.connect(self.left_button_clicked)
        right_button = QPushButton("RIGHT")
        right_button.clicked.connect(self.right_button_clicked)

        self.layout.addWidget(left_button)
        self.layout.addWidget(QLabel(task_string))
        self.layout.addWidget(right_button)
        self.setLayout(self.layout)

class Done_Widget(Task_Widget):
    def __init__(self, task_string: str=''):
        super().__init__()

        self.layout = QHBoxLayout()

        left_button = QPushButton("LEFT")
        left_button.clicked.connect(self.left_button_clicked)

        self.layout.addWidget(left_button)
        self.layout.addWidget(QLabel(task_string))
        self.layout.addWidget(QLabel())
        self.setLayout(self.layout)
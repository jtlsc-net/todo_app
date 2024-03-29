from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

# Widget class for columns in app.
# Contains pointers to right and left columns
class Column_Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.left = None
        self.right = None

    def paintEvent(self, event):
        # Needed for stylesheets on QWidget subclasses
        painter = QPainter(self)
        option = QStyleOption()
        option.initFrom(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, option, painter, self)


    def set_left(self, new_left: QWidget):
        self.left = new_left

    def set_right(self, new_right: QWidget):
        self.right = new_right
    
    def get_left(self):
        if self.left != None:
            return self.left
        else:
            return None
    
    def get_right(self):
        if self.right != None:
            return self.right
        else:
            return None
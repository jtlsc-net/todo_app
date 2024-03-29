from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from Task_Widget import *
from Column_Widget import *

class Tasks_List():
    def __init__(self, task_list: list=[]):
        self.task_list = task_list
    
    def add_task(self, task: str):
        self.task_list.append(task)

    def get_task_list(self) -> list:
        return self.task_list  #watch out for copy or not
    


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        
        todo_list = Tasks_List(['eat', 'sleep', 'code', 'poop', 'eat ice cream', 'nail salon'])
        doing_list = Tasks_List(['cry'])
        done_list = Tasks_List(['leetcode', 'apply'])


        screen = app.primaryScreen()

        self.setWindowTitle("todo app")
        self.setMinimumSize(int(screen.size().width() * 0.5), int(screen.size().height() * 0.5))

        self.h_layout = QHBoxLayout()
        self.todo_layout = QVBoxLayout()
        self.doing_layout = QVBoxLayout()
        self.done_layout = QVBoxLayout()

        for count, task in enumerate(todo_list.get_task_list()):
            self.todo_layout.addWidget(Task_Widget(0, task))
            if count == 4:
                break
        
        for count, task in enumerate(doing_list.get_task_list()):
            self.doing_layout.addWidget(Task_Widget(1, task))

        for count, task in enumerate(done_list.get_task_list()):
            self.done_layout.addWidget(Task_Widget(2, task))
        
        todo_widget = Column_Widget()
        todo_widget.setObjectName("todo_box")
        todo_widget.setStyleSheet("QWidget#todo_box { border: 1px solid black; border-radius: 15px;}")
        todo_widget.setLayout(self.todo_layout)

        doing_widget = Column_Widget()
        doing_widget.setObjectName("doing_box")
        doing_widget.setStyleSheet("QWidget#doing_box { border: 1px solid black; border-radius: 15px;}")
        doing_widget.setLayout(self.doing_layout)

        done_widget = Column_Widget()
        done_widget.setObjectName("done_box")
        done_widget.setStyleSheet("QWidget#done_box { border: 1px solid black; border-radius: 15px;}")
        done_widget.setLayout(self.done_layout)

        todo_widget.set_right(doing_widget)
        doing_widget.set_left(todo_widget)
        doing_widget.set_right(done_widget)
        done_widget.set_left(doing_widget)

        self.h_layout.addWidget(todo_widget)
        self.h_layout.addWidget(doing_widget)
        self.h_layout.addWidget(done_widget)

        h_widget = QWidget()
        h_widget.setLayout(self.h_layout)
        self.setCentralWidget(h_widget)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
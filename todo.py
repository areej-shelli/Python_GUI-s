import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QHBoxLayout, QLineEdit, QPushButton, QListWidget, QMessageBox
)
from PyQt5.QtGui import QFont

TASK_FILE = "tasks.txt"

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do App")
        self.setGeometry(100, 100, 400, 350)
        self.setStyleSheet(self.dark_style())

        font = QFont("Arial", 10)

        self.layout = QVBoxLayout()

        self.task_input = QLineEdit()
        self.task_input.setFont(font)
        self.task_input.setPlaceholderText("Enter a new task...")

        self.add_button = QPushButton("➕ Add")
        self.add_button.setFont(font)
        self.add_button.clicked.connect(self.add_task)

        self.task_list = QListWidget()
        self.task_list.setFont(QFont("Arial", 10))

        self.delete_button = QPushButton("🗑 Delete Selected")
        self.delete_button.setFont(font)
        self.delete_button.clicked.connect(self.delete_task)

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.task_input)
        input_layout.addWidget(self.add_button)

        self.layout.addLayout(input_layout)
        self.layout.addWidget(self.task_list)
        self.layout.addWidget(self.delete_button)

        self.setLayout(self.layout)

        self.load_tasks()

    def add_task(self):
        task = self.task_input.text()
        if task:
            self.task_list.addItem(task)
            self.task_input.clear()
            self.save_tasks()
        else:
            QMessageBox.warning(self, "Warning", "Please enter a task!")

    def delete_task(self):
        selected = self.task_list.currentRow()
        if selected >= 0:
            self.task_list.takeItem(selected)
            self.save_tasks()
        else:
            QMessageBox.warning(self, "Warning", "Please select a task to delete!")

    def save_tasks(self):
        tasks = []
        for i in range(self.task_list.count()):
            tasks.append(self.task_list.item(i).text())
        with open(TASK_FILE, "w", encoding="utf-8") as f:
            f.write("\n".join(tasks))

    def load_tasks(self):
        if os.path.exists(TASK_FILE):
            with open(TASK_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    task = line.strip()
                    if task:
                        self.task_list.addItem(task)

    def dark_style(self):
        return """
        QWidget {
            background-color: #2b2b2b;
            color: #eeeeee;
        }
        QLineEdit {
            padding: 6px;
            border: 1px solid #555;
            border-radius: 6px;
            background-color: #3c3f41;
            color: #fff;
        }
        QPushButton {
            background-color: #5c9ded;
            color: white;
            padding: 8px;
            border: none;
            border-radius: 6px;
        }
        QPushButton:hover {
            background-color: #4a89dc;
        }
        QListWidget {
            background-color: #3c3f41;
            border: 1px solid #555;
            border-radius: 6px;
        }
        """

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())

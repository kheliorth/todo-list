from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QLineEdit, QPushButton, QMessageBox
import sys
import os

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("To-Do List")
        self.setGeometry(100, 100, 400, 300)

        # Основной макет
        layout = QVBoxLayout()

        # Поле ввода
        self.entry = QLineEdit(self)
        layout.addWidget(self.entry)

        # Кнопки
        button_layout = QHBoxLayout()
        self.add_button = QPushButton("Добавить", self)
        self.add_button.clicked.connect(self.add_task)
        button_layout.addWidget(self.add_button)

        self.done_button = QPushButton("Выполнено", self)
        self.done_button.clicked.connect(self.mark_task_done)
        button_layout.addWidget(self.done_button)

        self.delete_button = QPushButton("Удалить", self)
        self.delete_button.clicked.connect(self.delete_task)
        button_layout.addWidget(self.delete_button)

        layout.addLayout(button_layout)

        # Список задач
        self.task_list = QListWidget(self)
        layout.addWidget(self.task_list)

        self.setLayout(layout)
        self.show_tasks()

    def load_tasks(self):
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as file:
                return [line.strip().split("|") for line in file.readlines()]
        return []

    def save_tasks(self, tasks):
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write("|".join(task) + "\n")

    def show_tasks(self):
        self.task_list.clear()
        tasks = self.load_tasks()
        for i, (task, status) in enumerate(tasks, 1):
            self.task_list.addItem(f"{i}. [{'x' if status == 'done' else ' '}] {task}")

    def add_task(self):
        task = self.entry.text()
        if task:
            tasks = self.load_tasks()
            tasks.append([task, "undone"])
            self.save_tasks(tasks)
            self.show_tasks()
            self.entry.clear()
        else:
            QMessageBox.warning(self, "Ошибка", "Введите задачу!")

    def mark_task_done(self):
        selected = self.task_list.currentRow()
        if selected >= 0:
            tasks = self.load_tasks()
            tasks[selected][1] = "done"
            self.save_tasks(tasks)
            self.show_tasks()
        else:
            QMessageBox.warning(self, "Ошибка", "Выберите задачу!")

    def delete_task(self):
        selected = self.task_list.currentRow()
        if selected >= 0:
            tasks = self.load_tasks()
            tasks.pop(selected)
            self.save_tasks(tasks)
            self.show_tasks()
        else:
            QMessageBox.warning(self, "Ошибка", "Выберите задачу!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())
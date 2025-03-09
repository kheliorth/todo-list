import tkinter as tk
from tkinter import messagebox
import os

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            return [line.strip().split("|") for line in file.readlines()]
    return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write("|".join(task) + "\n")

def show_tasks():
    task_list.delete(0, tk.END)
    tasks = load_tasks()
    for i, (task, status) in enumerate(tasks, 1):
        task_list.insert(tk.END, f"{i}. [{'x' if status == 'done' else ' '}] {task}")

def add_task():
    task = entry.get()
    if task:
        tasks = load_tasks()
        tasks.append([task, "undone"])
        save_tasks(tasks)
        show_tasks()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Ошибка", "Введите задачу!")

def mark_task_done():
    selected = task_list.curselection()
    if selected:
        tasks = load_tasks()
        index = selected[0]
        tasks[index][1] = "done"
        save_tasks(tasks)
        show_tasks()
    else:
        messagebox.showwarning("Ошибка", "Выберите задачу!")

def delete_task():
    selected = task_list.curselection()
    if selected:
        tasks = load_tasks()
        index = selected[0]
        tasks.pop(index)
        save_tasks(tasks)
        show_tasks()
    else:
        messagebox.showwarning("Ошибка", "Выберите задачу!")

# Создание окна
root = tk.Tk()
root.title("To-Do List")

# Поле ввода
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Кнопки
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Добавить", command=add_task)
add_button.grid(row=0, column=0, padx=5)

done_button = tk.Button(button_frame, text="Выполнено", command=mark_task_done)
done_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(button_frame, text="Удалить", command=delete_task)
delete_button.grid(row=0, column=2, padx=5)

# Список задач
task_list = tk.Listbox(root, width=50, height=15)
task_list.pack(pady=10)

# Загрузка задач при запуске
show_tasks()

# Запуск приложения
root.mainloop()
# tasks.txt будет хранить список задач
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

def show_tasks(tasks):
    if not tasks:
        print("Список задач пуст.")
    else:
        print("Ваши задачи:")
        for i, (task, status) in enumerate(tasks, 1):
            print(f"{i}. [{'x' if status == 'done' else ' '}] {task}")

def add_task(tasks):
    task = input("Введите новую задачу: ")
    tasks.append([task, "undone"])
    print("Задача добавлена!")

def mark_task_done(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Введите номер задачи для отметки как выполненной: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index][1] = "done"
            print("Задача отмечена как выполненная!")
        else:
            print("Неверный номер задачи.")
    except ValueError:
        print("Пожалуйста, введите число.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Введите номер задачи для удаления: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            print("Задача удалена!")
        else:
            print("Неверный номер задачи.")
    except ValueError:
        print("Пожалуйста, введите число.")

def main():
    tasks = load_tasks()
    while True:
        print("\nМеню:")
        print("1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Отметить задачу как выполненную")
        print("4. Удалить задачу")
        print("5. Выйти")
        choice = input("Выберите действие: ")
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Задачи сохранены. Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if name == "__main__":
    main()
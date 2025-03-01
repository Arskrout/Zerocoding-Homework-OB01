from datetime import datetime

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = datetime.strptime(deadline, '%Y-%m-%d')
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = 'Completed' if self.completed else 'Pending'
        return f"Task: {self.description}, Deadline: {self.deadline.date()}, Status: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def complete_task(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_completed()
                return True
        return False

    def show_pending_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def show_all_tasks(self):
        return self.tasks

# Пример использования TaskManager
manager = TaskManager()
manager.add_task("Buy groceries", "2025-03-05")
manager.add_task("Finish report", "2025-03-10")
manager.complete_task("Buy groceries")

print("Pending tasks:")
for task in manager.show_pending_tasks():
    print(task)

print("\nAll tasks:")
for task in manager.show_all_tasks():
    print(task)

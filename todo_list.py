class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "status": "Pending"})

    def list_tasks(self):
        return self.tasks

    def mark_completed(self, task_name):
        for task in self.tasks:
            if task["task"] == task_name:
                task["status"] = "Completed"
                return True
        return False

    def clear_tasks(self):
        self.tasks.clear()
    
    def add_task(self, task):
        if any(t["task"] == task for t in self.tasks):
            return False  # Task already exists
        self.tasks.append({"task": task, "status": "Pending"})
        return True

    def mark_completed(self, task_name):
        for task in self.tasks:
            if task["task"] == task_name:
                task["status"] = "Completed"
                return True  # Task marked as completed
        return False  # Task not found

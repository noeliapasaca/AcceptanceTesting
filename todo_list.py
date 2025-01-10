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

    def edit_task(self, old_task, new_task):
        for task in self.tasks:
            if task["task"] == old_task:
                task["task"] = new_task
                return True
        return False  # Task not found

    def filter_tasks(self, status):
        # Correctly filter tasks by status
        return [task for task in self.tasks if task["status"] == status]



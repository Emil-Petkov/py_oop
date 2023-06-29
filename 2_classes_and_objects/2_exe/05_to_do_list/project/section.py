from typing import List


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[str] = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        remove_counter = 0
        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                remove_counter += 1

        return f"Cleared {remove_counter} tasks."

    def view_section(self):
        result = f"Section {self.name}:\n"
        for task in self.tasks:
            result += task.details() + "\n"

        return result.strip()

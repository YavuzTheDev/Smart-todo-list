class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, priority='Low', due_date=None):
        task = {
            'name': name,
            'priority': priority,
            'due_date': due_date,
            'completed': False
        }
        self.tasks.append(task)

    def remove_task(self, name):
        self.tasks = [task for task in self.tasks if task['name'] != name]

    def mark_completed(self, name):
        for task in self.tasks:
            if task['name'] == name:
                task['completed'] = True

    def get_overdue_tasks(self):
        return [task for task in self.tasks if task['due_date'] and task['due_date'] < datetime.now()]

    def __str__(self):
        output = ''
        for task in self.tasks:
            status = 'Done' if task['completed'] else 'Pending'
            output += f"{task['name']} - {task['priority']} - {status}\n"
        return output

# Kullanım
todo_list = TodoList()
todo_list.add_task('Python öğren', 'High', datetime(2023, 12, 31))
todo_list.add_task('Projeyi bitir')
print(todo_list)

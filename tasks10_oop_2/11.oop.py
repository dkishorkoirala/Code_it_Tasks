class TaskManager:
    def __init__(self, user_name, task_list=[]):
        self.username = user_name
        self.task_list = task_list

    def add_task(self, task):
        self.task_list.append(task)
        print(f"Task: '{task}' added successfully")
        return self.task_list

    def remove_task(self, task):
        if task in self.task_list:
            self.task_list.remove(task)
            return f"Task: '{task}' removed successfully"
        else:
            return "Task not found"

    def view_task(self):
        for task in self.task_list:
            return self.task_list


t1 = TaskManager("ram")
print(t1.add_task("Do homework"))
# print(t1.view_task())
print(t1.add_task("Do coding"))
print(t1.add_task("Sleep"))
print(t1.view_task())
print(t1.remove_task("Sleep"))
print(t1.view_task())
print(t1.remove_task("help"))
print(t1.view_task())

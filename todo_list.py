tasks = []

def add_task(task):
    """Adds a new task to the list."""
    tasks.append(task)
    return f"Task '{task}' added."

def view_tasks():
    """Returns all tasks in the list."""
    if not tasks:
        return "No tasks available."
    return "\n".join(f"{i + 1}. {task}" for i, task in enumerate(tasks))

def update_task(index, new_task):
    """Updates the task at the given index."""
    try:
        old_task = tasks[index]
        tasks[index] = new_task
        return f"Task '{old_task}' updated to '{new_task}'."
    except IndexError:
        return "Error: Task index out of range."

def delete_task(index):
    """Deletes the task at the given index."""
    try:
        task = tasks.pop(index)
        return f"Task '{task}' deleted."
    except IndexError:
        return "Error: Task index out of range."

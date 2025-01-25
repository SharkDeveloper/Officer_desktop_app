from .models import Task
from .setup import SessionLocal
from datetime import date

# Create a new task
def create_task(title, description=None, image_path=None, due_date=None, repeat_period=None):
    session = SessionLocal()
    try:
        task = Task(
            title=title,
            description=description,
            image_path=image_path,
            due_date=due_date,
            repeat_period=repeat_period,
            status=False  # Default status: Not Completed
        )
        session.add(task)
        session.commit()
        session.refresh(task)
        return task
    finally:
        session.close()

# Read all tasks
def get_all_tasks():
    session = SessionLocal()
    try:
        return session.query(Task).all()
    finally:
        session.close()

# Get a single task by ID
def get_task_by_id(task_id):
    session = SessionLocal()
    try:
        return session.query(Task).filter(Task.id == task_id).first()
    finally:
        session.close()

# Update an existing task
def update_task(task_id, title=None, description=None, image_path=None, due_date=None, repeat_period=None, status=None):
    session = SessionLocal()
    try:
        task = session.query(Task).filter(Task.id == task_id).first()
        if not task:
            return None

        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if image_path is not None:
            task.image_path = image_path
        if due_date is not None:
            task.due_date = due_date
        if repeat_period is not None:
            task.repeat_period = repeat_period
        if status is not None:
            task.status = status

        session.commit()
        session.refresh(task)
        return task
    finally:
        session.close()

# Delete a task
def delete_task(task_id):
    session = SessionLocal()
    try:
        task = session.query(Task).filter(Task.id == task_id).first()
        if not task:
            return False

        session.delete(task)
        session.commit()
        return True
    finally:
        session.close()

# Mark a task as completed
def mark_task_as_completed(task_id):
    return update_task(task_id, status=True)

# Get tasks due today
def get_due_tasks():
    session = SessionLocal()
    try:
        today = date.today()
        return session.query(Task).filter(Task.due_date == today, Task.status == False).all()
    finally:
        session.close()
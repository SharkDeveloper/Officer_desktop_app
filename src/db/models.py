from sqlalchemy import Column, Integer, String, Text, Date, Boolean
from sqlalchemy.sql import func
from .setup import Base

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    image_path = Column(String, nullable=True)  # Path to the associated image file
    due_date = Column(Date, nullable=False)
    repeat_period = Column(String, nullable=True)  # e.g., "daily", "weekly", "monthly"
    status = Column(Boolean, default=False)  # False = Not Completed, True = Completed
    created_at = Column(Date, default=func.current_date())
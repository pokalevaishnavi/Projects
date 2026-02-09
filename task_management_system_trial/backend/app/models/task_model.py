from sqlalchemy import Column, Integer, String, Date, ForeignKey
from core.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    status = Column(String, default="Pending")
    due_date = Column(Date)
    assigned_user = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True 
)

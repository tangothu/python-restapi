from datetime import datetime
from config import db, ma


class Task(db.Model):
    __tablename__ = "task"
    task_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32))
    duedate = db.Column(
        db.Date, default=datetime.utcnow
    )


class TaskSchema(ma.ModelSchema):
    class Meta:
        model = Task
        sqla_session = db.session

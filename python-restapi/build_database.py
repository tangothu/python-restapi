import os
from config import db
from models import Task

# Data to initialize database with
TASKS = [
    {"title": "Do 100 JIRAs"},
    {"title": "Review 999 lines of code"},
    {"title": "Sleep"},
]

# Delete database file if it exists currently
if os.path.exists("tasks.db"):
    os.remove("tasks.db")

# Create the database
db.create_all()

# iterate over the PEOPLE structure and populate the database
for task in TASKS:
    p = Task(title=task.get("title"))
    db.session.add(p)

db.session.commit()

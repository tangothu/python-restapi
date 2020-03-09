"""
This is the tasks module and supports all the REST actions for the
tasks data
"""

from flask import make_response, abort
from config import db
from models import Task, TaskSchema
from datetime import datetime

def read_all():
    """
    This function responds to a request for /api/tasks
    with the complete lists of tasks

    :return:        json string of list of tasks
    """
    # Create the list of tasks from our data
    tasks = Task.query.order_by(Task.title).all()

    # Serialize the data for the response
    task_schema = TaskSchema(many=True)
    data = task_schema.dump(tasks)
    return data


def read_one(task_id):
    """
    This function responds to a request for /api/tasks/{task_id}
    with one matching task from tasks

    :param task_id:   Id of task to find
    :return:            task matching id
    """
    # Get the task requested
    task = Task.query.filter(Task.task_id == task_id).one_or_none()

    # Did we find a task?
    if task is not None:

        # Serialize the data for the response
        task_schema = TaskSchema()
        data = task_schema.dump(task)
        return data

    # Otherwise, nope, didn't find that task
    else:
        abort(
            404,
            "Task not found for Id: {task_id}".format(task_id=task_id),
        )


def create(task):
    """
    This function creates a new task in the tasks structure
    based on the passed in task data

    :param task:  task to create in tasks structure
    :return:        201 on success, 406 on task exists
    """
    title = task.get("title")
    duedate = task.get("duedate")
    existing_task = (
        Task.query.filter(Task.title == title)
        .one_or_none()
    )

    # Can we insert this task?
    if existing_task is None:

        # Create a task instance using the schema and the passed in task
        schema = TaskSchema()
        print(duedate)
        datetime_object = datetime.strptime(duedate, '%m/%d/%Y')
        task["duedate"] = datetime_object.strftime('%Y-%m-%d')

        new_task = schema.load(task, session=db.session)

        # Add the task to the database
        db.session.add(new_task)
        db.session.commit()

        # Serialize and return the newly created task in the response
        data = schema.dump(new_task)
        return data, 201

    # Otherwise, nope, task exists already
    else:
        abort(
            409,
            "Task {title} exists already".format(
                title=title
            ),
        )


def update(task_id, task):
    """
    This function updates an existing task in the tasks structure
    Throws an error if a task with the name we want to update to
    already exists in the database.

    :param task_id:   Id of the task to update in the tasks structure
    :param task:      task to update
    :return:            updated task structure
    """
    # Get the task requested from the db into session
    update_task = Task.query.filter(
        Task.task_id == task_id
    ).one_or_none()

    # Try to find an existing task with the same name as the update
    title = task.get("title")

    existing_task = (
        Task.query.filter(Task.title == title)
        .one_or_none()
    )

    # Are we trying to find a task that does not exist?
    if update_task is None:
        abort(
            404,
            "Task not found for Id: {task_id}".format(task_id=task_id),
        )

    # Would our update create a duplicate of another task already existing?
    elif (
        existing_task is not None and existing_task.task_id != task_id
    ):
        abort(
            409,
            "Task {title} exists already".format(
                title=title
            ),
        )

    # Otherwise go ahead and update!
    else:

        # turn the passed in task into a db object
        schema = TaskSchema()
        update = schema.load(task, session=db.session)

        # Set the id to the task we want to update
        update.task_id = update_task.task_id

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated task in the response
        data = schema.dump(update_task)

        return data, 200


def delete(task_id):
    """
    This function deletes a task from the tasks structure

    :param task_id:   Id of the task to delete
    :return:            200 on successful delete, 404 if not found
    """
    # Get the task requested
    task = Task.query.filter(Task.task_id == task_id).one_or_none()

    # Did we find a task?
    if task is not None:
        db.session.delete(task)
        db.session.commit()
        return make_response(
            "Task {task_id} deleted".format(task_id=task_id), 200
        )

    # Otherwise, nope, didn't find that task
    else:
        abort(
            404,
            "Task not found for Id: {task_id}".format(task_id=task_id),
        )

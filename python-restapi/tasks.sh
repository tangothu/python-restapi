#!/bin/bash
# file: tasks.sh


tasks() {
    if [[ $1 == "list" ]]; then
        if [[ -z "$2" ]]; then
            echo "No argument supplied"
            echo "Getting all tasks" >> /tmp/python_restapi_logfile.log
            command curl -X GET --header "Accept: application/json" "http://localhost:5000/api/tasks"
        else
            if [[ $2 == "--expiring-today" ]]; then
                echo "Getting tasks with ${2}" >> /tmp/python_restapi_logfile.log
                command curl -X GET --header "Accept: application/json" "http://localhost:5000/api/tasks-expiring"
            fi
        fi

    elif [[ $1 == "done" ]]; then
        task_id=$2
        echo "Done with task id ${task_id}" >> /tmp/python_restapi_logfile.log
        command curl -X DELETE --header "Accept: text/html" "http://localhost:5000/api/tasks/${task_id}"
    elif [[ $1 == "add" ]]; then
        task_title=$2
        task_time=$3
        echo "Adding new task ${task_title} with due date ${task_time}" >> /tmp/python_restapi_logfile.log
        printf -v payload '{"title": "%s", "duedate": "%s"}' "${task_title}" "${task_time}"
        echo "$payload"
        echo "${payload}"
        command curl -X POST --header "Content-Type: application/json" --header "Accept: application/json" -d "${payload}" 'http://localhost:5000/api/tasks'
    else
        echo "no operation needed"
    fi
}


tasks

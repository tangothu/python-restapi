#!/bin/bash
# file: tasks.sh

tasks() {
    if [[ $1 == "list" ]]; then
        command curl -X GET --header "Accept: application/json" "http://localhost:5000/api/tasks"
    elif [[ $1 == "done" ]]; then
        task_id=$2
        echo "Done with task id ${task_id}"
        command curl -X DELETE --header "Accept: text/html" "http://localhost:5000/api/tasks/${task_id}"
    elif [[ $1 == "add" ]]; then
        task_title=$2
        task_time=$3
        echo "Adding new task ${task_title}"
        printf -v payload '{"title": "%s", "duedate": "%s"}' "${task_title}" "${task_time}"
        echo "$payload"
        echo "${payload}"
        command curl -X POST --header "Content-Type: application/json" --header "Accept: application/json" -d "${payload}" 'http://localhost:5000/api/tasks'
    else
        echo "no operation needed"
    fi
}


tasks

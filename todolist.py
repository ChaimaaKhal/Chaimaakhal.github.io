# Import necessary modules
import os
import json

# Define the file name for storing the to-do list
FILENAME = 'todolist.json'

# Function to load the to-do list from the file
def load_todolist():
    # Check if the file exists
    if os.path.isfile(FILENAME):
        # Open the file and load the to-do list from the JSON data
        with open(FILENAME, 'r') as f:
            todolist = json.load(f)
    else:
        # If the file does not exist, create an empty to-do list
        todolist = []

    return todolist

# Function to save the to-do list to the file
def save_todolist(todolist):
    # Open the file and write the to-do list to the file as JSON data
    with open(FILENAME, 'w') as f:
        json.dump(todolist, f)

# Function to add a task to the to-do list
def add_task(todolist):
    # Prompt the user for the task description
    task = input('Enter task description: ')

    # Add the task to the to-do list
    todolist.append({'description': task, 'completed': False})

    # Save the updated to-do list to the file
    save_todolist(todolist)

# Function to edit a task in the to-do list
def edit_task(todolist):
    # Display the current tasks in the to-do list
    list_tasks(todolist)

    # Prompt the user for the task number to edit
    task_num = int(input('Enter task number to edit: ')) - 1

    # Prompt the user for the new task description
    new_task = input('Enter new task description: ')

    # Update the task in the to-do list
    todolist[task_num]['description'] = new_task

    # Save the updated to-do list to the file
    save_todolist(todolist)

# Function to delete a task from the to-do list
def delete_task(todolist):
    # Display the current tasks in the to-do list
    list_tasks(todolist)

    # Prompt the user for the task number to delete
    task_num = int(input('Enter task number to delete: ')) - 1

    # Remove the task from the to-do list
    del todolist[task_num]

    # Save the updated to-do list to the file
    save_todolist(todolist)

# Function to list all tasks in the to-do list
def list_tasks(todolist):
    # Display a header for the list of tasks
    print('\nTask List\n--------')

    # Loop through each task in the to-do list and display its description
    for i, task in enumerate(todolist):
        print(f'{i+1}. {task["description"]}')

# Function to display the menu options
def display_menu():
    # Display the menu options
    print('\nMenu\n----')
    print('1. List tasks')
    print('2. Add task')
    print('3. Edit task')
    print('4. Delete task')
    print('5. Exit')

# Main function to run the to-do list application
def main():
    # Load the to-do list from the file
    todolist = load_todolist()

    # Display the menu options and prompt the user for their choice
    while True:
        display_menu

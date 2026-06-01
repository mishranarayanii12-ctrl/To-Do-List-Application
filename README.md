# To-Do List CLI App

A simple command-line to-do list I built to get better at Python file handling and JSON.
Nothing fancy — just a tool that actually saves your tasks so they don't disappear 
when you close the terminal.

## Why I built this
I kept forgetting assignments and wanted to practice Python beyond just print statements. 
This was my first time working with JSON files and it took me embarrassingly long to get 
the data persisting correctly, but figured it out eventually.

## What it does
- Add tasks with a due date and priority (High / Medium / Low)
- View all pending tasks sorted by due date
- See overdue tasks highlighted separately when you open the app
- Mark tasks as done or delete them
- Filter tasks by priority level
- Everything saves to a local JSON file so nothing is lost on exit

## How to run it

Make sure you have Python 3 installed, then:

git clone https://github.com/NarayaniMishra/todo-app
cd todo-app
python todo.py

No external libraries needed. Uses only Python built-ins.

## What I learned
- Reading and writing JSON with the json module
- Structuring code into functions instead of dumping everything in one block
- Handling edge cases like empty task lists and invalid date formats

## Possible improvements (haven't done these yet)
- A proper GUI using tkinter
- Export tasks to PDF
- Reminder notifications

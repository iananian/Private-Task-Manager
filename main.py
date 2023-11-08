import tkinter as tk
from tkinter import messagebox

# Create and initialize the list to store tasks
tasks = []

# Function to add a task
def add_task():
    task = task_entry.get()
    deadline = deadline_entry.get()
    if task:
        tasks.append((task, deadline, False))
        list_tasks()
        task_entry.delete(0, tk.END)
        deadline_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to list all tasks
def list_tasks():
    task_list.delete(0, tk.END)
    for i, (task, deadline, completed) in enumerate(tasks, start=1):
        task_status = "✓" if completed else " "
        task_list.insert(tk.END, f"{i}. {task} (Deadline: {deadline}) [{task_status}]")

# Function to mark a task as completed
def complete_task():
    selected_task = task_list.curselection()
    if selected_task:
        index = selected_task[0]
        task_index = int(index.split(".")[0]) - 1
        tasks[task_index] = (tasks[task_index][0], tasks[task_index][1], True)
        list_tasks()

# Function to sort tasks by deadline
def sort_by_deadline():
    tasks.sort(key=lambda x: x[1])
    list_tasks()

# Create a Tkinter window
window = tk.Tk()
window.title("Task Manager")

# Create and configure GUI elements
task_label = tk.Label(window, text="Task:")
task_entry = tk.Entry(window)
deadline_label = tk.Label(window, text="Deadline:")
deadline_entry = tk.Entry(window)
add_button = tk.Button(window, text="Add Task", command=add_task)
list_button = tk.Button(window, text="List Tasks", command=list_tasks)
complete_button = tk.Button(window, text="Complete Task", command=complete_task)
sort_button = tk.Button(window, text="Sort by Deadline", command=sort_by_deadline)
task_list = tk.Listbox(window)

# Place GUI elements on the window
task_label.pack()
task_entry.pack()
deadline_label.pack()
deadline_entry.pack()
add_button.pack()
list_button.pack()
complete_button.pack()
sort_button.pack()
task_list.pack()

# Run the Tkinter main loop
window.mainloop()

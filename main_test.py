import tkinter as tk
from tkinter import messagebox
import pickle

# 파일에 저장되는 tasks 데이터를 담을 파일 이름.
TASKS_FILE = "tasks_data.pkl"

# task를 저장하기 위한 list를 제작한다.
tasks = []

# 파일에서 tasks를 불러오기 위한 기능.
def load_tasks():
    global tasks
    try:
        with open(TASKS_FILE, 'rb') as file:
            tasks = pickle.load(file)
    except FileNotFoundError:
        print("save된 file을 찾을 수 없음. 새로운 파일을 생성함.")

# tasks를 파일에 저장하기 위한 기능.
def save_tasks():
    with open(TASKS_FILE, 'wb') as file:
        pickle.dump(tasks, file)

# 태스크를 추가하기 위한 기능.
def add_task():
    try:
        # 데드라인은 년, 월, 일을 각각 작성하기 위해 list로 작성.
        deadline = [0, 0, 0]

        # 요소들을 input받음.
        task = entry_task.get()

        # Task의 Deadline을 작성 / 양식 : '년 월 일'
        deadline_input = entry_deadline.get()
        deadline[0], deadline[1], deadline[2] = map(int, deadline_input.split())

        order = len(tasks)

        # input받은 요소들을 tasks 리스트에 저장
        # status의 기본값은 false
        if task:
            tasks.append((task, deadline, False, order))
            update_task_list()
            entry_task.delete(0, tk.END)  # 입력 필드 초기화
            entry_deadline.delete(0, tk.END)  # 입력 필드 초기화
        else:
            messagebox.showwarning("경고", "Task를 작성하지 않았습니다.")
    except ValueError:
        messagebox.showwarning("에러", "유효한 날짜를 입력하세요.")

# 모든 태스크를 보여주기 위한 기능.
def update_task_list():
    task_listbox.delete(0, tk.END)
    for i, task_info in enumerate(tasks):
        if not task_info[2]:  # Status가 False인 경우에만 표시
            task_listbox.insert(tk.END, f"Task: {task_info[0]} Deadline: {task_info[1]} Status: {task_info[2]}")

# 데드라인순으로 태스크를 정렬하기 위한 기능.
def sort_by_deadline():
    # order값을 기준으로 tasks를 정렬
    tasks_sort_deadline = sorted(tasks, key=lambda x: (x[1][0], x[1][1], x[1][2]))

    # tasks를 리스트업
    task_listbox.delete(0, tk.END)
    for i, task_info in enumerate(tasks_sort_deadline):
        if not task_info[2]:  # Status가 False인 경우에만 표시
            task_listbox.insert(tk.END, f"Task: {task_info[0]} Deadline: {task_info[1]} Status: {task_info[2]}")

# 태스크를 complete로 표시하기 위한 기능.
def complete_task():
    try:
        status = int(entry_complete.get())
        if 0 <= status < len(tasks):
            if not tasks[status][2]:
                tasks[status] = (tasks[status][0], tasks[status][1], True, tasks[status][3])
                messagebox.showinfo("알림", "Task가 완료로 표시됨")
                update_task_list()
            else:
                messagebox.showinfo("알림", "이미 완료된 Task")
        else:
            messagebox.showwarning("경고", "유효한 번호가 아님")
    except ValueError:
        messagebox.showwarning("에러", "유효한 숫자를 입력하세요.")

# 시작
load_tasks()

root = tk.Tk()
root.title("Task Manager")

# Task 입력
label_task = tk.Label(root, text="Task의 내용을 작성")
label_task.pack()
entry_task = tk.Entry(root)
entry_task.pack()

# Deadline 입력
label_deadline = tk.Label(root, text="Task의 Deadline을 작성 / 양식 : '년 월 일'")
label_deadline.pack()
entry_deadline = tk.Entry(root)
entry_deadline.pack()

# Task 추가 버튼
button_add_task = tk.Button(root, text="Task 추가", command=add_task)
button_add_task.pack()

# Task 리스트
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack()

# Order 순으로 정렬 버튼
button_sort_order = tk.Button(root, text="Order순으로 Task를 정렬", command=update_task_list)
button_sort_order.pack()

# Deadline 순으로 정렬 버튼
button_sort_deadline = tk.Button(root, text="Deadline순으로 Task를 정렬", command=sort_by_deadline)
button_sort_deadline.pack()

# Task 완료 버튼
label_complete = tk.Label(root, text="완료할 Task의 번호를 선택")
label_complete.pack()
entry_complete = tk.Entry(root)
entry_complete.pack()
button_complete_task = tk.Button(root, text="Task를 완료", command=complete_task)
button_complete_task.pack()

# 종료 버튼
button_exit = tk.Button(root, text="Task Manager를 종료", command=root.destroy)
button_exit.pack()

root.mainloop()

# 끝나고 나서
save_tasks()
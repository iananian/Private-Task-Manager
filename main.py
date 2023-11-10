# import tkinter as tk
# from tkinter import messagebox


# task를 저장하기 위한 list를 제작한다.
tasks = []


# 태스크를 추가하기 위한 기능.
def add_task():
    # 데드라인은 년, 월, 일을 각각 작성하기 위해 list로 작성.
    deadline = [0, 0, 0]

    # 요소들을 input받음.
    task = input("Task의 내용을 작성\n")
    deadline[0], deadline[1], deadline[2] = input("Task의 Deadline을 작성 / 양식 : '년 월 일'\n").split(" ")
    order = len(tasks)

    # input받은 요소들을 tasks리스트에 저장
    # status의 기본값은 false
    if task:
        tasks.append((task, deadline, False, order))
    else:
        print("경고, Task를 작성")


# 모든 태스크를 보여주기 위한 기능.
def sort_by_order():
    # tasks를 리스트업
    for i in tasks:
        if i[2] == False:
            print("Task: ", i[0], "Deadline: ", i[1], "Status: ", i[2])


# 데드라인순으로 태스크를 정렬하기 위한 기능.
def sort_by_deadline():
        # order값을 기준으로 tasks를 정렬
    tasks_sort_deadline = sorted(tasks, key=lambda x: (x[1][0], x[1][1], x[1][2]))

    # tasks를 리스트업
    for i in tasks_sort_deadline:
        if i[2] == False:
            print("Task: ", i[0], "Deadline: ", i[1], "Status: ", i[2])


# 태스크를 완료로 표시하기 위한 기능.
def complete_task():
    global tasks
    if not tasks:
        print("할 일이 없음")
        return

    try:
        status = int(input("완료할 Task의 번호를 선택\n"))
        if 0 <= status < len(tasks):
            if not tasks[status][2]:
                tasks[status] = (tasks[status][0], tasks[status][1], True, tasks[status][3])
                print("Task가 완료로 표시됨")
            else:
                print("이미 완료된 Task")
        else:
            print("유효한 번호가 아님")
    except ValueError:
        print("유효한 숫자를 입력")

# 시작
while True:
    select = input("1. Task를 추가\n2. Order순으로 Task를 정렬\n3. Deadline순으로 Task를 정렬\n4. Task를 완료\n")
    if select == '1':
        add_task()
    elif select == '2':
        sort_by_order()
    elif select == '3':
        sort_by_deadline()
    elif select == '4':
        complete_task()
    else:
        print("Invalid input. Please enter a valid option.")    






# # GUI 윈도우를 열음.
# window = tk.Tk()
# window.title("Task Manager")

# # GUI 요소들을 만듦.
# task_label = tk.Label(window, text="Task:")
# task_entry = tk.Entry(window)
# deadline_label = tk.Label(window, text="Deadline:")
# deadline_entry = tk.Entry(window)
# add_button = tk.Button(window, text="Add Task", command=add_task)
# list_button = tk.Button(window, text="List Tasks", command=list_tasks)
# complete_button = tk.Button(window, text="Complete Task", command=complete_task)
# sort_button = tk.Button(window, text="Sort by Deadline", command=sort_by_deadline)
# task_list = tk.Listbox(window)

# # GUI 요소들을 배치함.
# task_label.pack()
# task_entry.pack()
# deadline_label.pack()
# deadline_entry.pack()
# add_button.pack()
# list_button.pack()
# complete_button.pack()
# sort_button.pack()
# task_list.pack()

# # GUI를 실행함.
# window.mainloop()
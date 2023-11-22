# 필요한 요소 import
import tkinter
import tkinter as tk
import tkinter.ttk
import tkinter.messagebox
import pickle


# 파일 이름 설정
# 세이브 파일을 주고 받으려면 메인 폴더에 아래 만든 파일을 넣고 빼면 됨 XD
TASKS_FILE = "tasks_data.pkl"


# GUI 설정
window=tkinter.Tk()



window.title("Task Manager")
window.geometry("560x720")
# 태스크 매니저의 특징에 맞게 많은 테스크를 수용할 수 있도록
# 아래로는 사이즈를 늘릴 수 있게 만듦
window.resizable(False, True)

window["bg"] = "#444444"


# task 저장을 위한 리스트를 제작
tasks = []


# 저장된 task 로드
def load_tasks():
    # 함수 내에서 전역 변수를 수정하기 위한 작업.
    global tasks
    # 에러 없을시 시도
    try:
        # 저장된 파일을 tasks 배열에 대입
        with open(TASKS_FILE, 'rb') as file:
            tasks = pickle.load(file)
       
        # 현재의 listbox 삭제
        if(list_task.size()!=0):
            list_task.delete(0,list_task.size()-1)


        # 로드한 task 배치
        for i in range(0,len(tasks)):
            list_task.insert(i,"Task "+str(i+1)+" : "+tasks[i][0]+" || DeadLine : "+str(tasks[i][1])+"년 " +str(tasks[i][2])+"월 "+str(tasks[i][3])+"일")
    # 파일이 없을시 출력
    except FileNotFoundError:
        tkinter.messagebox.showerror("error", "save된 file을 찾을 수 없음.")


# 파일에 tasks 배열 저장
def save_tasks():
    global tasks
    with open(TASKS_FILE, 'wb') as file:
        pickle.dump(tasks, file)


# task 추가 함수
def add_task():  
    global tasks
    # task 제목이 없다면 작성 지시
    if (entry_task.get()==""):    
        tkinter.messagebox.showerror("error", "task가 입력되지 않음.")
        return
   
    # listbox에 task 삽입
    list_task.insert(len(tasks),"Task "+str(len(tasks)+1)+" : "+entry_task.get()+" || DeadLine : "+task_year.get()+"년 " +task_month.get()+"월 "+task_date.get()+"일")


    # tasks 배열에 추가
    tasks.append((entry_task.get(),int(task_year.get()),int(task_month.get()),int(task_date.get())))


# 추가된 순으로 정렬
def sort_order():
    # task가 없을시 종료
    if (len(tasks)==0):
        tkinter.messagebox.showerror("error", "Task를 작성 후 시도.")
        return
   
    # 현재 listbox 삭제
    list_task.delete(0,list_task.size()-1)


    # tasks 배열속 요소를 대입 (처음 만든 리스트 tasks 는 원래 추가된 순으로 작성됨)
    for i in range(0,len(tasks)):
        list_task.insert(i,"Task "+str(i+1)+" : "+tasks[i][0]+" || DeadLine : "+str(tasks[i][1])+"년 " +str(tasks[i][2])+"월 "+str(tasks[i][3])+"일")


# 마감기한순 정렬
def sort_deadline():
    if (len(tasks)==0):
        tkinter.messagebox.showerror("error", "Task를 작성 후 시도.")
        return
   
    list_task.delete(0,list_task.size()-1)

    # tasks배열을 deadline순으로 정렬한 새로운 배열 생성
    deadline_tasks=sorted(tasks,key=lambda x: (x[1], x[2], x[3]))

    # 배열 대입
    for i in range(0,len(tasks)):
        list_task.insert(i,"Task "+str(i+1)+" : "+deadline_tasks[i][0]+" || DeadLine : "+str(deadline_tasks[i][1])+"년 " +str(deadline_tasks[i][2])+"월 "+str(deadline_tasks[i][3])+"일")


# task 완료
def task_complete():
    # 선택된 task index 구하기
    selected_task_index=list_task.curselection()
    # 선택 없을시 종료
    if (selected_task_index==()):
        tkinter.messagebox.showerror("error", "task를 선택 후 시도.")
        return
    
    # 그 위치의 listbox를 삭제
    list_task.delete(selected_task_index[0],selected_task_index[0])
    
    # task를 기록한 배열에서 삭제
    del tasks[selected_task_index[0]]

# GUI 배치

task_y_pos = 40
label_task=tkinter.Label(window, text="Task : ", bg="#444444", fg = "#ffffff")
label_task.pack()
label_task.place(x=40,y=task_y_pos)


entry_task = tk.Entry(window, width=30)
entry_task.pack()
entry_task.place(x=100,y=task_y_pos)


deadline_y_pos = 80

label_deadline = tk.Label(window, text="Deadline : ", bg="#444444", fg = "#ffffff")
label_deadline.pack()
label_deadline.place(x=40,y=deadline_y_pos)


from datetime import datetime

today_year = datetime.today().year
year_values=[str(i) for i in range(2023, 2034)]
task_year=tkinter.ttk.Combobox(window,state="readonly",width=4,height=15, values=year_values)
task_year.place(x=100,y=deadline_y_pos)
task_year.set(today_year)


label_year=tkinter.Label(window, text="년", bg="#444444", fg = "#ffffff")
label_year.place(x=140,y=deadline_y_pos)
label_month=tkinter.Label(window, text="월", bg="#444444", fg = "#ffffff")
label_month.place(x=220,y=deadline_y_pos)
label_day=tkinter.Label(window, text="일", bg="#444444", fg = "#ffffff")
label_day.place(x=300,y=deadline_y_pos)

today_month = datetime.today().month
month_values=[str(i) for i in range(1, 13)]
task_month=tkinter.ttk.Combobox(window,state="readonly",width=2,height=15, values=month_values)
task_month.place(x=180,y=deadline_y_pos)
task_month.set(today_month)

today_date = datetime.today().day
date_values=[str(i) for i in range(1,32)]
task_date=tkinter.ttk.Combobox(window,state="readonly",width=2,height=15, values=date_values)
task_date.place(x=260,y=deadline_y_pos)
task_date.set(today_date)

config_x_pos = 430
button_add = tkinter.Button(window, text="Add Task",width=9, command=add_task, bd=0, bg="#ffffff")
button_add.place(x=340,y=40)


button_save=tkinter.Button(window,text="Task Save",width=11, command=save_tasks, bd=0, bg="#ffffff")
button_save.place(x=config_x_pos,y=40)


button_load=tkinter.Button(window,text="Task Load",width=11, command=load_tasks, bd=0, bg="#ffffff")
button_load.place(x=config_x_pos,y=80)


list_task = tkinter.Listbox(selectmode='extended',width=50, height=0, bd=0)
list_task.place(x=40,y=120)


button_sort_order = tkinter.Button(window,text="Sort Order",width=11, command=sort_order, bd=0, bg="#ffffff")
button_sort_order.place(x=config_x_pos,y=120)


button_sort_deadline = tkinter.Button(window, text="Sort DeadLine",width=11, command=sort_deadline, bd=0, bg="#ffffff")
button_sort_deadline.place(x=config_x_pos,y=160)


button_complete = tkinter.Button(window, text="Task Complete",width=11, command=task_complete, bd=0, bg="#ffffff")
button_complete.place(x=config_x_pos,y=240)


load_tasks()

window.mainloop()

save_tasks()
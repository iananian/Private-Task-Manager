# 필요한 요소 import
import tkinter
import tkinter as tk
import tkinter.ttk
import pickle


# 파일 이름 설정
TASKS_FILE = "tasks_data.pkl"


# GUI 설정
window=tkinter.Tk()


window.title("Task Manager")
window.geometry("640x400")
window.resizable(False, True)


# task 저장을 위한 배열
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
        print("save된 file을 찾을 수 없음.")


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
        print("Task를 입력하세요!!")
        return
   
    # listbox에 task 삽입
    list_task.insert(len(tasks),"Task "+str(len(tasks)+1)+" : "+entry_task.get()+" || DeadLine : "+task_year.get()+"년 " +task_month.get()+"월 "+task_date.get()+"일")


    # tasks 배열에 추가
    tasks.append((entry_task.get(),int(task_year.get()),int(task_month.get()),int(task_date.get())))


# 추가된 순으로 정렬
def sort_order():
    # task가 없을시 종료
    if (len(tasks)==0):
        print("Task를 입력하세요!!")
        return
   
    # 현재 listbox 삭제
    list_task.delete(0,list_task.size()-1)


    # tasks 배열속 요소를 대입 (tasks는 원래 추가된 순)
    for i in range(0,len(tasks)):
        list_task.insert(i,"Task "+str(i+1)+" : "+tasks[i][0]+" || DeadLine : "+str(tasks[i][1])+"년 " +str(tasks[i][2])+"월 "+str(tasks[i][3])+"일")


# 마감기한순 정렬
def sort_deadline():
    if (len(tasks)==0):
        print("Task를 입력하세요!!")
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
        print("task를 선택하세요!!")
        return
   
    # 그 위치의 listbox를 삭제
    list_task.delete(selected_task_index[0],selected_task_index[0])
       
     # task를 기록한 배열에서 삭제
    del tasks[selected_task_index[0]]


# GUI 배치
label_task=tkinter.Label(window, text="Task 내용")
label_task.pack()


entry_task = tk.Entry(window, width=30)
entry_task.pack()


label_deadline = tk.Label(window, text="Deadline (년 월 일)")
label_deadline.pack()


year_values=[str(i) for i in range(2023, 2034)]
task_year=tkinter.ttk.Combobox(window,state="readonly",width=4,height=15, values=year_values)
task_year.place(x=197,y=75)
task_year.set("2023")


label_year=tkinter.Label(window, text="년")
label_year.place(x=250,y=75)
label_month=tkinter.Label(window, text="년")
label_month.place(x=341,y=75)
label_day=tkinter.Label(window, text="년")
label_day.place(x=425,y=75)


month_values=[str(i) for i in range(1, 13)]
task_month=tkinter.ttk.Combobox(window,state="readonly",width=2,height=15, values=month_values)
task_month.place(x=298,y=75)
task_month.set("1")


date_values=[str(i) for i in range(1,32)]
task_date=tkinter.ttk.Combobox(window,state="readonly",width=2,height=15, values=date_values)
task_date.place(x=382,y=75)
task_date.set("1")


button_add = tkinter.Button(window, text="Add Task",width=9, command=add_task)
button_add.place(x=250,y=106)


button_save=tkinter.Button(window,text="Task Save",width=9, command=save_tasks)
button_save.place(x=540,y=150)


button_load=tkinter.Button(window,text="Task Load",width=9, command=load_tasks)
button_load.place(x=540,y=190)


list_task = tkinter.Listbox(selectmode='extended',width=50, height=0)
list_task.place(x=118,y=146)


button_sort_order = tkinter.Button(window,text="Sort Order",width=11, command=sort_order)
button_sort_order.place(x=370,y=106)


button_sort_deadline = tkinter.Button(window, text="Sort DeadLine",width=11, command=sort_deadline)
button_sort_deadline.place(x=480,y=106)


button_complete = tkinter.Button(window, text="Task Complete",width=11, command=task_complete)
button_complete.place(x=140,y=106)


window.mainloop()

import tkinter
import tkinter as tk
import tkinter.ttk
from tkinter import *




window=tkinter.Tk()


window.title("Task Manager")
window.geometry("640x400")
window.resizable(False, False)


#///////////////d  여기까지 기본 설정




# listbox속 task제목,데드라인을 기록하기 위한 2차원 배열 (편의를 위해 크기 100, 나머지 요소를 10000으로 설정)
list_tasks=[]
for i in range(100):
    list_tasks.append([])
    for j in range(4):
        list_tasks[i].append(10000)


# deadline순으로 정렬할떄 사용할 2차원 배열
tasks = []
for i in range(100):
    tasks.append([])
    for j in range(4):
        tasks[i].append(10000)


# 현재 task의 수
task_num=0
# 추가된 순으로 정렬하기 위한 변수, 추가될때마다 항상 증가
task_order=0
# list_tasks 배열의 순서를 위한 변수
task_order_1=0
# 추가된 순으로 정렬할때 사용할 2차원 배열
lastest_tasks=[]
for i in range(100):
    lastest_tasks.append([])
    for j in range(5):
        lastest_tasks[i].append(10000)






# 연도가 윤년일때 일 수를 바꿈, 2월일때만 실행됨
def check_year(event):
    if int(task_year.get()) % 4 == 0 and int(task_year.get()) % 100 != 0:
        task_date["values"]=[str(i) for i in range(1,29)]
    elif int(task_year.get()) % 400 == 0:
        task_date["values"]=[str(i) for i in range(1,29)]
    else:
        task_date["values"]=[str(i) for i in range(1,30)]


# 2월일때는 위의 함수, 홀수달일땐 31일, 짝수달일땐 30일까지 설정
def change_date(event):
    if (int(task_month.get()) % 2 ==1 ):
        task_date["values"]=[str(i) for i in range(1,32)]
    elif (int(task_month.get()) % 2 ==0 and int(task_month.get()) // 2 !=1):
        task_date["values"]=[str(i) for i in range(1,31)]
    elif (int(task_month.get()) // 2 ==1):
        check_year(event)




def add_task():   # task 추가 함수
    if (entry_task.get()==""):    # task 제목이 없다면 작성 지시
        print("Task를 입력하세요!!")
        return
    global task_num   # task 수를 세기 위함
    global task_order   # task를 추가된 순으로 정렬하기 위한 변수
    global task_order_1
    global tasks
    global lastest_tasks
    global list_tasks


    # task 리스트의 task_num번째에 입력된 변수로 task 추가
    list_task.insert(task_num, "Task "+str(task_num+1)+" : "+entry_task.get()+" || DeadLine : "+task_year.get()+"년 " +task_month.get()+"월 "+task_date.get()+"일")
   
    # task를 기록하기 위한 배열
    list_tasks[task_order_1]=[entry_task.get(),task_year.get(),task_month.get(),task_date.get()]
    task_order_1=task_order_1+1
   
   
    # task를 입력순, 데드라인순으로 정렬하기 위한 배열에 저장, 위의 list_tasks에서 가져옴
    task_order_()
   
    # task 추가했으니 task_num에 1을 더함
    task_num=task_num+1
    # task가 입력된 횟수가 늘어남
    task_order=task_order+1
   
   
# 리스트에 추가된 순으로 정렬
def sort_order():
    # 위의 변수 사용
    global task_num
    global task_order
    global tasks
    global lastest_tasks


    # task가 없을시 출력
    if (task_num==0):
        print("Task를 입력하세요!!")
        return
   
    # 현재 task_lists 배열의 값을 대입
    task_order_()
   
    # try 실행, 에러시 밑으로
    try:
        # 우선 현재 listbox를 모두 삭제
        k=list_task.size()-1
        list_task.delete(0,k)
        task_num=0






        # task_order순으로 정렬, 추가될때마다 1씩 증가하는 값
        lastest_tasks.sort(key=lambda x: x[4])   # 정렬


        # 추가된 순으로 출력, 판단은 lastest_tasks의 task_order로 판단(이 값은 항상 증가)
        for i in range(0,k+1):  # 원래의 listbox만큼 반복
            # listbox에 값 추가, task_num 더하기
            list_task.insert(task_num, "Task "+str(task_num+1)+" : "+str(lastest_tasks[i][0])+" || DeadLine : "+str(lastest_tasks[i][1])+"년 " +str(lastest_tasks[i][2])+"월 "+str(lastest_tasks[i][3])+"일")
            task_num=task_num+1
    # 에러 발생시 실행
    except IndexError:
        print("Task를 입력하세요!!")


# 기한 순으로 정렬
def sort_deadline():
    # 위의 변수 사용
    global task_num
    global task_order
    global tasks
    global lastest_tasks


    # task가 0일때 출력
    if (task_num==0):
        print("Task를 입력하세요!!")
        return
       
    # 기록된 list_tasks를 대입
    task_order_()
   
    # listbox 모두 삭제
    k=list_task.size()-1
    list_task.delete(0,list_task.size()-1)
    task_num=0


   


    # 날자순으로 정렬
    tasks.sort(key=lambda x: (x[1],x[2],x[3]))
       
    # listbox에 표시
    for i in range(0,k+1):
        list_task.insert(task_num, "Task "+str(task_num+1)+" : "+str(tasks[i][0])+" || DeadLine : "+str(tasks[i][1])+"년 " +str(tasks[i][2])+"월 "+str(tasks[i][3])+"일")
        task_num=task_num+1
       




# 선택된 task를 완료(삭제)
def task_complete():
    # 위의 변수를 사용
    global task_num
    global task_order
    global tasks
    global lastest_tasks
    global task_order_1


    # try 아래의 명령를 실행, 에러시 except으로
    try:
        # 선택된 task의 위치를 나타냄
        selected_task_index=list_task.curselection()
        # 그 위치의 listbox를 삭제
        list_task.delete(selected_task_index[0],selected_task_index[0])
       
        # task수가 줄음
        task_num=task_num-1


        # list_tasks 수 줄음
        task_order_1=task_order_1-1


        # task를 기록한 배열에서 삭제
        del list_tasks[selected_task_index[0]]


       
       
        # 삭제 후 다시 배열에 값 넣음
        task_order_()


       
   
       




       
    # 에러시 출력
    except IndexError:
        print("Task를 선택하세요!!")




# 기록된 list_tasks 배열의 값을 대입
def task_order_():
    global task_num
    global task_order
    global tasks
    global lastest_tasks
    global list_tasks


    # tasks,lastest_tasks 초기화
    for j in range(100):
            for k in range(4):
                tasks[j][k]=10000
            for k in range(5):
                lastest_tasks[j][k]=10000


    # 대입
    for i in range(0,list_task.size()):
       


        tasks[i][0]=list_tasks[i][0]
        tasks[i][1]=int(list_tasks[i][1])
        tasks[i][2]=int(list_tasks[i][2])
        tasks[i][3]=int(list_tasks[i][3])
   
        lastest_tasks[i][0]=list_tasks[i][0]
        lastest_tasks[i][1]=int(list_tasks[i][1])
        lastest_tasks[i][2]=int(list_tasks[i][2])
        lastest_tasks[i][3]=int(list_tasks[i][3])
        lastest_tasks[i][4]=task_order


        task_order=task_order+1


       


   




# GUI 배치
label_task=tkinter.Label(window, text="Task 내용")
label_task.pack()


entry_task = tk.Entry(window, width=30)
entry_task.pack()


label_deadline = tk.Label(window, text="Deadline (년 월 일)")
label_deadline.pack()


year_values=[str(i) for i in range(2023, 2034)]
task_year=tkinter.ttk.Combobox(window,state="readonly",width=4,height=15, values=year_values)
task_year.pack()
task_year.place(x=197,y=75)
task_year.set("2023")


label_date=tkinter.Label(window, text="년              월              일")
label_date.place(x=255,y=75)


month_values=[str(i) for i in range(1, 13)]
task_month=tkinter.ttk.Combobox(window,state="readonly",width=2,height=15, values=month_values)
task_month.pack()
task_month.place(x=298,y=75)
task_month.set("1")


date_values=[str(i) for i in range(1,32)]
task_date=tkinter.ttk.Combobox(window,state="readonly",width=2,height=15, values=date_values)
task_date.place(x=382,y=75)
task_date.set("1")


button_add = tkinter.Button(window, text="Task 추가",width=9, command=add_task)
button_add.place(x=277,y=106)






list_task = tkinter.Listbox(selectmode='extended',width=50, height=10)
list_task.place(x=118,y=146)




button_sort_order = tkinter.Button(window,text="Sort Order",width=11, command=sort_order)
button_sort_order.place(x=370,y=106)


button_sort_deadline = tkinter.Button(window, text="Sort DeadLine",width=11, command=sort_deadline)
button_sort_deadline.place(x=480,y=106)


button_complete = tkinter.Button(window, text="Task Complete",width=11, command=task_complete)
button_complete.place(x=140,y=106)




# 년도, 월이 바뀔때 함수 실행
task_year.bind("<<ComboboxSelected>>", change_date)
task_month.bind("<<ComboboxSelected>>", change_date)


window.mainloop()

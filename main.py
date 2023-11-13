# pickle모듈을 이용해 데이터를 로컬로 저장. / web서비스시 서버에 저장하도록 수정 가능.
import pickle

# 파일에 저장되는 tasks 데이터를 담을 파일 이름.
TASKS_FILE = "tasks_data.pkl"

# task를 저장하기 위한 list를 제작.
# task의 양식은 다음 과 같음. (task, deadline, status, order)
tasks = []

# 파일에서 tasks를 불러오기 위한 기능.
def load_tasks():
    # 함수 내에서 전역 변수를 수정하기 위한 작업.
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
    # 데드라인은 년, 월, 일을 각각 작성하기 위해 list로 작성.
    deadline = [0, 0, 0]
    
    # 요소들을 input받음.
    task = input("Task의 내용을 작성\n")
    try:
        deadline[0], deadline[1], deadline[2] = input("Task의 Deadline을 작성 / 양식 : '년 월 일'\n").split(" ")
    except ValueError:
        deadline[0], deadline[1], deadline[2] = input("Task의 Deadline을 다시 작성 / 양식 : '년 월 일'\n").split(" ")

    # input받은 요소들을 tasks리스트에 저장
    # status의 기본값은 false
    if task:
        tasks.append((task, deadline, False))
    else:
        print("경고, Task를 작성")


# 모든 태스크를 보여주기 위한 기능.
def sort_by_order():
    # tasks를 리스트업
    for i in tasks:
        if i[2] == False:
            print("Task:", i[0], "Deadline:", i[1], "Status:", i[2])


# 데드라인순으로 태스크를 정렬하기 위한 기능.
def sort_by_deadline():
    # order값을 기준으로 tasks를 정렬
    tasks_sort_deadline = sorted(tasks, key=lambda x: (x[1][0], x[1][1], x[1][2]))

    # tasks를 리스트업
    for i in tasks_sort_deadline:
        if i[2] == False:
            print("Task:", i[0], "Deadline:", i[1], "Status:", i[2])


# 태스크를 complete로 표시하기 위한 기능.
def complete_task():
    # 함수 내에서 전역 변수를 수정하기 위한 작업.
    global tasks

    # tasks가 없다면 return하기 위한 기능.
    if not tasks:
        print("Task가 없음")
        return

    # 예외 경우가 발생하면 처리하기 위해 try를 이용.
    try:
        status = int(input("완료할 Task의 번호를 선택\n"))
        if status >= 0 and status <= len(tasks):
            if not tasks[status][2]:
                del tasks[status]
                print("Task가 완료로 표시됨")
            else:
                print("이미 완료된 Task")
        else:
            print("유효한 번호가 아님")
    except ValueError:
        print("유효한 숫자를 입력")


# 시작
load_tasks()
while True:
    select = input("1. Task를 추가\n2. Order순으로 Task를 정렬\n3. Deadline순으로 Task를 정렬\n4. Task를 완료\n5. Task Manager를 종료\n")
    if select == '1':
        add_task()
    elif select == '2':
        sort_by_order()
    elif select == '3':
        sort_by_deadline()
    elif select == '4':
        complete_task()
    elif select == '5':
        break
    else:
        print("유효하지 않은 input. 알맞은 option을 선택.")    


# 끝나고 나서
save_tasks()
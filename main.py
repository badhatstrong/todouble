from tkinter import *
from tkinter import messagebox


def new_task():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
        task_list.write(task)
        task_list.write('\n')
    else:
        messagebox.showwarning("warning", "Please enter some task.")


def delete_task():
    with open("todo.txt", "r") as t:
        lines = t.readlines()
    with open("todo.txt", "w") as t:
        for line in lines:
            if item != line:
                t.write(line)
    lb.delete(ANCHOR)


ws = Tk()
ws.geometry('500x700+500+200')
ws.title('Simple To-Do List')
ws.config(bg='#223441')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=32,
    height=14,
    font=('Times', 12),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
)
lb.pack(side=LEFT, fill=BOTH)

task_list = open('./todo.txt', 'r+')

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('times', 24)
)

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font='times 10',
    bg='#c5f776',
    padx=20,
    pady=10,
    command=new_task
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font='times 10',
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=delete_task
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

ws.mainloop()

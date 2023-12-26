"""
TODO | Read books | 2022-05-26 16:00
TODO | Buy groceries | 2022-05-26 17:00
TODO | Clean my room | 2022-05-27 16:00
TODO | Go to gym | 2022-05-28 16:00


Programi ilk acinca iki sey yapicak:
1) Zamani gecen TODO satirlari icin uyari verecek. "You missed the following TODOs:"
2) O gunku ileri zamanli TODOlari hatirlatacak. "You have the following TODOs today: ..."

What do you want to do? add
What? Read books
When? 2022-05-26 16:00
Added your TODO

What do you want to do? add
What? ...
When? ...
Added your TODO

What do you want to do? search
What? gym
Found TODO: Go to gym on 2022-05-28 at 16:00
What you you want with this TODO? done

Dosyada: DONE | Go to gym | 2022-05-28 16:00


What do you want to do? search
What? gym
Found TODO: Go to gym on 2022-05-28 at 16:00
What you you want with this TODO? delete
Dosyada o satiri sil.

What do you want to do? clear-done
Done statusundekileri silecek.(arşiv)
Alert before TODO.*
"""


import tkinter
import tkinter.messagebox
import pickle
from todo import TodoItem
import datetime
from tkcalendar import Calendar


root = tkinter.Tk()
root.title("To-Do List by Arca")


def add_task():
    task_text = entry_task.get().strip()         # trim
    if task_text != "":
        timestamp = datetime.datetime.strptime(date_picker.get_date(), '%m/%d/%y')
        task = TodoItem(task_text, timestamp)
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")


def delete_task():
    selection = listbox_tasks.curselection()
    if len(selection) > 0:
        task_index = selection[0]    # "curselection" = current selection, why first index? [0]
        listbox_tasks.delete(task_index)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")


def load_task():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))    # "rb" = read binary
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")


def save_task():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))         # "wb" = write binary


frame_tasks = tkinter.Frame(root)
frame_tasks.pack()


listbox_tasks = tkinter.Listbox(frame_tasks, height=13, width=50)
listbox_tasks.pack(side=tkinter.LEFT)


scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)


# Code for more convenient scrollbar. Not fully understood how it works though.
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)


entry_task = tkinter.Entry(root, width=50)
entry_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)

date_picker = Calendar(root,selectmode = "day",year=2022,month=1,date=1)
date_picker.pack(pady=40)

button_add_task = tkinter.Button(root, text="Add Task", width=48, command=add_task)
button_add_task.pack()


button_delete_task = tkinter.Button(root, text="Delete Task", width=48, command=delete_task)
button_delete_task.pack()


button_load_task = tkinter.Button(root, text="Load Task", width=48, command=load_task)
button_load_task.pack()

button_save_task = tkinter.Button(root, text="Save Task", width=48, command=save_task)
button_save_task.pack()


root.mainloop()



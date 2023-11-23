from tkinter import *
from data import *
import os
d = 0.0
def add():
    taget = diem.get() + '-' + heso.get()
    save(taget)
    show()
def show():
    ds = read()
    listbox.delete(0, END)
    for i in ds:
        listbox.insert(END, i)
def xoa():
    with open(path, 'r') as f:
        lines = f.readlines()
        new_lines = lines[:-1]
        with open(path, 'w') as f:
                f.write("".join(new_lines))
    show()
def tinh():
    ds = read()
    listboxout.delete(0, END)
    for i in ds:
        x = ds[i][0]
        d = d + dictionary[x[0]]
    listboxout.insert(END, d)
root = Tk()
diem = StringVar()
heso = StringVar()
root.title('GPA')
root.minsize(width=400, height=300)
Label(root, text='GPA:', fg='blue', font=('cambria', 16)).grid(row=0)
listbox = Listbox(root, width=10, height=20)
listbox.grid(row=1, rowspan=3)
show()
Label(root, text='Nhap Diem:', fg='blue', font=('cambria', 8)).grid(row=1, column=1)
Entry(root, width=20, textvariable=diem).grid(row=1, column=2)
Label(root, text='Nhap So Tin Chi:', fg='blue', font=('cambria', 8)).grid(row=2, column=1)
Entry(root, width=20, textvariable=heso).grid(row=2, column=2)
button = Frame(root)
Button(button, text='Nhap', command=add).pack(side=LEFT)
Button(button, text='Tinh', command=tinh).pack(side=LEFT)
Button(button, text='Xoa', command=xoa).pack(side=LEFT)
Button(button, text='Thoat', command=root.quit).pack(side=LEFT)
button.grid(row=3, column=1)
listboxout = Listbox(root, width=20, height= 5)
listboxout.grid(row=3,column=2)
root.mainloop()
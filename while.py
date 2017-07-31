from tkinter import  Tk, StringVar, ttk
import tkinter.simpledialog
import tkinter.messagebox
from time import strftime
now = strftime( "%x %Z %X")
from tkinter import *
import  time;
import datetime

#importing the tk fxn from tkinter modual
anthony = Tk()
#config the window+ giving the title
anthony.title("ATTENDANCE REGISTER")
anthony.geometry()
anthony.configure(background="pink")
#creating frames

l_frame = Frame(anthony, width=1000, height=650, bd=8, relief="raised")
l_frame.pack(side=LEFT)
r_frame = Frame(anthony, width=350, height=650, bd=8, relief="raised")
r_frame.pack(side=RIGHT)
#frames in the left frame
l_frame1 = Frame(l_frame, width=1000, height=100, bd=8, relief="raised")
l_frame1.pack(side=TOP)
l_frame2 = Frame(l_frame, width=1000, height=550 , bd=8 , relief="raised")
l_frame2.pack()
#frames in the r.frames
r_frame1 = Frame(r_frame, width=350, height=215, bd=8, relief="raised")
r_frame1.pack(side=TOP)
r_frame2 = Frame(r_frame, width=350, height=415, bd=8, relief="raised")
r_frame2.pack()

#decrare variables
DateofOrder = StringVar()
value0 = StringVar()
value1 = StringVar()
value2 = StringVar()
value3 = StringVar()
value4 = StringVar()
value5 = StringVar()
value6 = StringVar()
value7 = StringVar()
value8 = StringVar()
value9 = StringVar()
value10 = StringVar()
value11 = StringVar()
value12 = StringVar()
#reset fxn
def Reset():
    value0.set("")
    value1.set("")
    value2.set("")
    value3.set("")
    value4.set("")
    value5.set("")
    value6.set("")
    value7.set("")
    value8.set("")
    value9.set("")
    value10.set("")

#exit fxn
def qExit():
    if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
        anthony.destroy()

anthony.protocol(qExit)
#anthony.mainloop()

#adding components to the top left frame
DateofOrder.set(time.strftime(" %d/%m/%Y"))

lbl = Label(l_frame1, font=('arial', 10, 'bold'), text="NO.", bd=16)
lbl.grid(row=0, column=0, sticky=W)
lblstudent = Label(l_frame1,font=('arial', 10, 'bold'), text="Student No.", bd=16)
lblstudent.grid(row=0, column=1, sticky=W)
lblsn = Label(l_frame1, font=("arial", 10, 'bold'), text="Student Name.", bd=16)
lblsn.grid(row=0, column=2, sticky=W)
lblcode = Label(l_frame1,font=('arial', 10, 'bold'), text="Course Code.", bd=16)
lblcode.grid(row=0, column=3, sticky=W)
#creating a drop box/list
box = ttk.Combobox(l_frame1 , textvariable=value0,state="readonly")
box['values'] = ('','/','l','o','a','s')
box.current(0)
box.grid(row=0,column=4)


#creating button

btfill= Button(l_frame1,text="Fill", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=0,column=5)

btreset= Button(l_frame1,text="Reset", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1,command= Reset).grid(row=0,column=6)

btquit= Button(l_frame1,text="EXIT", padx=2 , pady=2,bd=2,fg="red",font=('arial',10,'bold'), width=12,height=1,command= qExit).grid(row=0,column=7)

lbldet=Label(l_frame1,font=('arial',10,'bold'),textvariable=DateofOrder, padx=2,
             pady=2,fg="green",bg="white",relief='sunken')
lbldet.grid(row=0,column=8,sticky=W)


#row0
i=1;
value=0;
while i<= 11:
    lbl = Label(l_frame2, font=('arial', 10, 'bold'), text=i, bd=16)
    lbl.grid(row=i, column=0, sticky=W)
    lblstudent = Label(l_frame2,font=('arial', 10, 'bold'), text="3383", bd=16)
    lblstudent.grid(row=i, column=1, sticky=W)
    lblsn = Label(l_frame2, font=("arial", 10, 'bold'), text="Anthony", bd=16)
    lblsn.grid(row=i, column=2, sticky=W)
    lblcode = Label(l_frame2,font=('arial', 10, 'bold'), text="101E", bd=16)
    lblcode.grid(row=i, column=3, sticky=W)
    #creating a drop box/list
    box = ttk.Combobox(l_frame2 , textvariable=value1,state="readonly")
    box['values'] = ('','/','l','o','a','s')
    box.current(0)
    box.grid(row=i,column=4)


#creating button

    btfill= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=i,column=5)

    btreset= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=i,column=6)

    btexit= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=i,column=7)

    btexi= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=i,column=8)

    i+=1



anthony.mainloop()

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
''''
#frme image
cont = Canvas(r_frame2 , width=350, heght=415 , bg="black")
cont.grid(row=0 , column=0)
image1 = PhotoImage(file="2.jpg")
image = cont.create_image(200,200,image = image1)

#cont image
cont = Canvas(r_frame1 , width=350, heght=215 , bg="black")
cont.grid(row=0 , column=0)
image2 = PhotoImage(file="3.jpg")
image = cont.create_image(200,200,image = image2)


def pic1():
    image = cont.create_image(200,200,image = image2)
image3=PhotoImage(file="index.jpeg")
def pic1():
    image = cont.create_image(200,200,image = image3)

image4=PhotoImage(file="nm.jpeg")
def pic1():
    image = cont.create_image(200,200,image = image4)
image5=PhotoImage(file="images.jpeg")
def pic1():
    image = cont.create_image(200,200,image = image5)



'''




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

 #fill function

def fill():
    if value0.get()=="/":
        value0.set("/")
        value1.set("/")
        value2.set("/")
        value3.set("/")
        value4.set("/")
        value5.set("/")
        value6.set("/")
        value7.set("/")
        value8.set("/")
        value9.set("/")
        value10.set("/")
    elif(value0.get()=="s"):
        value0.set("s")
        value1.set("s")
        value2.set("s")
        value3.set("s")
        value4.set("s")
        value5.set("s")
        value6.set("s")
        value7.set("s")
        value8.set("s")
        value9.set("s")
        value10.set("s")
    elif(value0.get()=="l"):
        value0.set("l")
        value1.set("l")
        value2.set("l")
        value3.set("l")
        value4.set("l")
        value5.set("l")
        value6.set("l")
        value7.set("l")
        value8.set("l")
        value9.set("l")
        value10.set("l")
    elif(value0.get()=="o"):
        value0.set("o")
        value1.set("o")
        value2.set("o")
        value3.set("o")
        value4.set("o")
        value5.set("o")
        value6.set("o")
        value7.set("o")
        value8.set("o")
        value9.set("o")
        value10.set("o")
    elif(value0.get()=="a"):
        value0.set("a")
        value1.set("a")
        value2.set("a")
        value3.set("a")
        value4.set("a")
        value5.set("a")
        value6.set("a")
        value7.set("a")
        value8.set("a")
        value9.set("a")
        value10.set("a")
    elif(value0.get()==" "):
        value0.set(" ")
        value1.set(" ")
        value2.set(" ")
        value3.set(" ")
        value4.set(" ")
        value5.set(" ")
        value6.set(" ")
        value7.set(" ")
        value8.set(" ")
        value9.set(" ")
        value10.set(" ")


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

btfill= Button(l_frame1,text="Fill", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1,command=fill).grid(row=0,column=5)

btreset= Button(l_frame1,text="Reset", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1,command= Reset).grid(row=0,column=6)

btquit= Button(l_frame1,text="EXIT", padx=2 , pady=2,bd=2,fg="red",font=('arial',10,'bold'), width=12,height=1,command= qExit).grid(row=0,column=7)

lbldet=Label(l_frame1,font=('arial',10,'bold'),textvariable=DateofOrder, padx=2,
             pady=2,fg="green",bg="white",relief='sunken')
lbldet.grid(row=0,column=8,sticky=W)


#row0

lbl = Label(l_frame2, font=('arial', 10, 'bold'), text="1.", bd=16)
lbl.grid(row=0, column=0, sticky=W)
lblstudent = Label(l_frame2,font=('arial', 10, 'bold'), text="3383", bd=16)
lblstudent.grid(row=0, column=1, sticky=W)
lblsn = Label(l_frame2, font=("arial", 10, 'bold'), text="Anthony", bd=16)
lblsn.grid(row=0, column=2, sticky=W)
lblcode = Label(l_frame2,font=('arial', 10, 'bold'), text="101E", bd=16)
lblcode.grid(row=0, column=3, sticky=W)
#creating a drop box/list
box = ttk.Combobox(l_frame2 , textvariable=value1,state="readonly")
box['values'] = ('','/','l','o','a','s')
box.current(0)
box.grid(row=0,column=4)


#creating button

btfill= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=0,column=5)

btreset= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=0,column=6)

btexit= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=0,column=7)

btexi= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=0,column=8)





#row1

lbl = Label(l_frame2, font=('arial', 10, 'bold'), text="2", bd=16)
lbl.grid(row=1, column=0, sticky=W)
lblstudent = Label(l_frame2,font=('arial', 10, 'bold'), text="3382", bd=16)
lblstudent.grid(row=1, column=1, sticky=W)
lblsn = Label(l_frame2, font=("arial", 10, 'bold'), text="Ann", bd=16)
lblsn.grid(row=1, column=2, sticky=W)
lblcode = Label(l_frame2,font=('arial', 10, 'bold'), text="101E", bd=16)
lblcode.grid(row=1, column=3, sticky=W)
#creating a drop box/list
box = ttk.Combobox(l_frame2 , textvariable=value2,state="readonly")
box['values'] = ('','/','l','o','a','s')
box.current(0)
box.grid(row=1,column=4)


#creating button

btfill= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=1,column=5)

btreset= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=1,column=6)

btexit= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=1,column=7)

btexi= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=1,column=8)





#row2

lbl = Label(l_frame2, font=('arial', 10, 'bold'), text="3.", bd=16)
lbl.grid(row=2, column=0, sticky=W)
lblstudent = Label(l_frame2,font=('arial', 10, 'bold'), text="3380", bd=16)
lblstudent.grid(row=2, column=1, sticky=W)
lblsn = Label(l_frame2, font=("arial", 10, 'bold'), text="Anthon", bd=16)
lblsn.grid(row=2, column=2, sticky=W)
lblcode = Label(l_frame2,font=('arial', 10, 'bold'), text="101E", bd=16)
lblcode.grid(row=2, column=3, sticky=W)
#creating a drop box/list
box = ttk.Combobox(l_frame2 , textvariable=value3,state="readonly")
box['values'] = ('','/','l','o','a','s')
box.current(0)
box.grid(row=2,column=4)


#creating button

btfill= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=2,column=5)

btreset= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=2,column=6)

btexit= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=2,column=7)

btexi= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=2,column=8)




#row3

lbl = Label(l_frame2, font=('arial', 10, 'bold'), text="4", bd=16)
lbl.grid(row=3, column=0, sticky=W)
lblstudent = Label(l_frame2,font=('arial', 10, 'bold'), text="338", bd=16)
lblstudent.grid(row=3, column=1, sticky=W)
lblsn = Label(l_frame2, font=("arial", 10, 'bold'), text="Anony", bd=16)
lblsn.grid(row=3, column=2, sticky=W)
lblcode = Label(l_frame2,font=('arial', 10, 'bold'), text="101E", bd=16)
lblcode.grid(row=3, column=3, sticky=W)
#creating a drop box/list
box = ttk.Combobox(l_frame2 , textvariable=value4,state="readonly")
box['values'] = ('','/','l','o','a','s')
box.current(0)
box.grid(row=3,column=4)


#creating button

btfill= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=3,column=5)

btreset= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=3,column=6)

btexit= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=3,column=7)

btexi= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=3,column=8)




#row4

lbl = Label(l_frame2, font=('arial', 10, 'bold'), text="4", bd=16)

lbl.grid(row=4, column=0, sticky=W)
lblstudent = Label(l_frame2,font=('arial', 10, 'bold'), text="3383", bd=16)
lblstudent.grid(row=4, column=1, sticky=W)
lblsn = Label(l_frame2, font=("arial", 10, 'bold'), text="Anthony", bd=16)
lblsn.grid(row=4, column=2, sticky=W)
lblcode = Label(l_frame2,font=('arial', 10, 'bold'), text="101E", bd=16)
lblcode.grid(row=4, column=3, sticky=W)
#creating a drop box/list
box = ttk.Combobox(l_frame2 , textvariable=value4,state="readonly")
box['values'] = ('','/','l','o','a','s')
box.current(0)
box.grid(row=4,column=4)


#creating button

btfill= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=4,column=5)

btreset= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=4,column=6)

btexit= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=4,column=7)

btexi= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=4,column=8)






#row5

lbl = Label(l_frame2, font=('arial', 10, 'bold'), text="5", bd=16)
lbl.grid(row=5, column=0, sticky=W)
lblstudent = Label(l_frame2,font=('arial', 10, 'bold'), text="33", bd=16)
lblstudent.grid(row=5, column=1, sticky=W)
lblsn = Label(l_frame2, font=("arial", 10, 'bold'), text="Anthoy", bd=16)
lblsn.grid(row=5, column=2, sticky=W)
lblcode = Label(l_frame2,font=('arial', 10, 'bold'), text="101E", bd=16)
lblcode.grid(row=5, column=3, sticky=W)
#creating a drop box/list
box = ttk.Combobox(l_frame2 , textvariable=value5,state="readonly")
box['values'] = ('','/','l','o','a','s')
box.current(0)
box.grid(row=5,column=4)


#creating button

btfill= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=5,column=5)

btreset= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=5,column=6)

btexit= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=5,column=7)

btexi= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=5,column=8)






#row6

lbl = Label(l_frame2, font=('arial', 10, 'bold'), text="6", bd=16)
lbl.grid(row=6, column=0, sticky=W)
lblstudent = Label(l_frame2,font=('arial', 10, 'bold'), text="3383", bd=16)
lblstudent.grid(row=6, column=1, sticky=W)
lblsn = Label(l_frame2, font=("arial", 10, 'bold'), text="Anthony", bd=16)
lblsn.grid(row=6, column=2, sticky=W)
lblcode = Label(l_frame2,font=('arial', 10, 'bold'), text="101E", bd=16)
lblcode.grid(row=6, column=3, sticky=W)
#creating a drop box/list
box = ttk.Combobox(l_frame2 , textvariable=value6,state="readonly")
box['values'] = ('','/','l','o','a','s')
box.current(0)
box.grid(row=6,column=4)


#creating button

btfill= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=6,column=5)

btreset= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=6,column=6)

btexit= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=6,column=7)

btexi= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=6,column=8)



#row7

lbl = Label(l_frame2, font=('arial', 10, 'bold'), text="7", bd=16)
lbl.grid(row=7, column=0, sticky=W)
lblstudent = Label(l_frame2,font=('arial', 10, 'bold'), text="3383", bd=16)
lblstudent.grid(row=7, column=1, sticky=W)
lblsn = Label(l_frame2, font=("arial", 10, 'bold'), text="Anthony", bd=16)
lblsn.grid(row=7, column=2, sticky=W)
lblcode = Label(l_frame2,font=('arial', 10, 'bold'), text="101E", bd=16)
lblcode.grid(row=7, column=3, sticky=W)
#creating a drop box/list
box = ttk.Combobox(l_frame2 , textvariable=value7,state="readonly")
box['values'] = ('','/','l','o','a','s')
box.current(0)
box.grid(row=7,column=4)


#creating button

btfill= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=7,column=5)

btreset= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=7,column=6)

btexit= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=7,column=7)

btexi= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=0,column=8)




#row8

lbl = Label(l_frame2, font=('arial', 10, 'bold'), text="8", bd=16)
lbl.grid(row=8, column=0, sticky=W)
lblstudent = Label(l_frame2,font=('arial', 10, 'bold'), text="3383", bd=16)
lblstudent.grid(row=8, column=1, sticky=W)
lblsn = Label(l_frame2, font=("arial", 10, 'bold'), text="Anthony", bd=16)
lblsn.grid(row=8, column=2, sticky=W)
lblcode = Label(l_frame2,font=('arial', 10, 'bold'), text="101E", bd=16)
lblcode.grid(row=8, column=3, sticky=W)
#creating a drop box/list
box = ttk.Combobox(l_frame2 , textvariable=value8,state="readonly")
box['values'] = ('','/','l','o','a','s')
box.current(0)
box.grid(row=8,column=4)


#creating button

btfill= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=8,column=5)

btreset= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=8,column=6)

btexit= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=8,column=7)

btexi= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=8,column=8)




#row9

lbl = Label(l_frame2, font=('arial', 10, 'bold'), text="9", bd=16)
lbl.grid(row=9, column=0, sticky=W)
lblstudent = Label(l_frame2,font=('arial', 10, 'bold'), text="3383", bd=16)
lblstudent.grid(row=9, column=1, sticky=W)
lblsn = Label(l_frame2, font=("arial", 10, 'bold'), text="Anthony", bd=16)
lblsn.grid(row=9, column=2, sticky=W)
lblcode = Label(l_frame2,font=('arial', 10, 'bold'), text="101E", bd=16)
lblcode.grid(row=9, column=3, sticky=W)
#creating a drop box/list
box = ttk.Combobox(l_frame2 , textvariable=value9,state="readonly")
box['values'] = ('','/','l','o','a','s')
box.current(0)
box.grid(row=9,column=4)


#creating button

btfill= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=9,column=5)

btreset= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=9,column=6)

btexit= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=9,column=7)

btexi= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=9,column=8)





#row10

lbl = Label(l_frame2, font=('arial', 10, 'bold'), text="10", bd=16)
lbl.grid(row=10, column=0, sticky=W)
lblstudent = Label(l_frame2,font=('arial', 10, 'bold'), text="3383", bd=16)
lblstudent.grid(row=10, column=1, sticky=W)
lblsn = Label(l_frame2, font=("arial", 10, 'bold'), text="Anthony", bd=16)
lblsn.grid(row=10, column=2, sticky=W)
lblcode = Label(l_frame2,font=('arial', 10, 'bold'), text="101E", bd=16)
lblcode.grid(row=10, column=3, sticky=W)
#creating a drop box/list
box = ttk.Combobox(l_frame2 , textvariable=value10,state="readonly")
box['values'] = ('','/','l','o','a','s')
box.current(0)
box.grid(row=10,column=4)


#creating button

btfill= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=10,column=5)

btreset= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=10,column=6)

btexit= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=10,column=7)

btexi= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=10,column=8)



'''

#row11

lbl = Label(l_frame2, font=('arial', 10, 'bold'), text="11", bd=16)
lbl.grid(row=11, column=0, sticky=W)
lblstudent = Label(l_frame2,font=('arial', 10, 'bold'), text="3383", bd=16)
lblstudent.grid(row=11, column=1, sticky=W)
lblsn = Label(l_frame2, font=("arial", 10, 'bold'), text="Anthony", bd=16)
lblsn.grid(row=11, column=2, sticky=W)
lblcode = Label(l_frame2,font=('arial', 10, 'bold'), text="101E", bd=16)
lblcode.grid(row=11, column=3, sticky=W)
#creating a drop box/list
box = ttk.Combobox(l_frame2 , textvariable=value11,state="readonly")
box['values'] = ('','/','l','o','a','s')
box.current(0)
box.grid(row=11,column=4)


#creating button

btfill= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=11,column=5)

btreset= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=11,column=6)

btexit= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=11,column=7)

btexi= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=11,column=8)




#row12

lbl = Label(l_frame2, font=('arial', 10, 'bold'), text="12", bd=16)
lbl.grid(row=12, column=0, sticky=W)
lblstudent = Label(l_frame2,font=('arial', 10, 'bold'), text="3383", bd=16)
lblstudent.grid(row=12, column=1, sticky=W)
lblsn = Label(l_frame2, font=("arial", 10, 'bold'), text="Anthony", bd=16)
lblsn.grid(row=12, column=2, sticky=W)
lblcode = Label(l_frame2,font=('arial', 10, 'bold'), text="101E", bd=16)
lblcode.grid(row=12, column=3, sticky=W)
#creating a drop box/list
box = ttk.Combobox(l_frame2 , textvariable=value12,state="readonly")
box['values'] = ('','/','l','o','a','s')
box.current(0)
box.grid(row=12,column=4)


#creating button

btfill= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=12,column=5)

btreset= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=12,column=6)

btexit= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=12,column=7)

btexi= Button(l_frame2,text=" ", padx=2 , pady=2,bd=2,fg="green",font=('arial',10,'bold'), width=12,height=1).grid(row=12,column=8)

'''



anthony.mainloop()

#keep the window alive/loop the code

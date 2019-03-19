import tkinter
import sys
from tkinter import Tk
from tkinter import *
#tkinter.NoDefaultRoot()
#####################################################################################################
# окно
aminok= Tk()

aminok.geometry('1650x900')
aminok.title("Запоминание аминокислот")
canvas = Canvas(aminok, width=1650, height=900, bg='green') # Холст. 0,0 - верхний левый угол.
#####################################
# ##################################################
title=Label(aminok,text='Выберите \n аланин')
title.config(bg='green',fg='white')
title.config(font=('helvetica', 40, 'bold italic'))
canvas.create_window(850,100, window=title)
#photo=PhotoImage(file='lena.gif')      #/home/gatupov/PycharmProjects/venv
#canvas.create_image(10, 10, image=photo, anchor=NW) # встроить изображение


##############################
#
# блок создания 6 кнопок
substance1 = Button(aminok,text='W', padx=100, pady=50)

substance1.config(width=5,height=5)
substance1.config(cursor='hand2')
substance1.config(bd=8, relief=RAISED)
substance1.config(bg='dark green', fg='white')
substance1.config(font=('helvetica', 20, 'italic'))
substance1.pack(padx=5, pady=5)
x1=500;
y1=350;

canvas.create_window(x1,y1, window=substance1)

substance2 = Button(aminok,text='L', padx=100, pady=50)

substance2.config(width=5,height=5)
substance2.config(cursor='hand2')
substance2.config(bd=8, relief=RAISED)
substance2.config(bg='dark green', fg='white')
substance2.config(font=('helvetica', 20, 'italic'))
substance2.pack(padx=5, pady=5)

dx=350;
dy=0;

canvas.create_window(x1+dx,y1+dy, window=substance2)

substance3 = Button(aminok,text='Q', padx=100, pady=50)

substance3.config(width=5,height=5)
substance3.config(cursor='hand2')
substance3.config(bd=8, relief=RAISED)
substance3.config(bg='dark green', fg='white')
substance3.config(font=('helvetica', 20, 'italic'))
substance3.pack(padx=5, pady=5)

dx=350*2;
dy=0;

canvas.create_window(x1+dx,y1+dy, window=substance3)

substance4 = Button(aminok,text='A', padx=100, pady=50)

substance4.config(width=5,height=5)
substance4.config(cursor='hand2')
substance4.config(bd=8, relief=RAISED)
substance4.config(bg='dark green', fg='white')
substance4.config(font=('helvetica', 20, 'italic'))
substance4.pack(padx=5, pady=5)

dx=0;
dy=350;

canvas.create_window(x1+dx,y1+dy, window=substance4)

substance5 = Button(aminok,text='H', padx=100, pady=50)

substance5.config(width=5,height=5)
substance5.config(cursor='hand2')
substance5.config(bd=8, relief=RAISED)
substance5.config(bg='dark green', fg='white')
substance5.config(font=('helvetica', 20, 'italic'))
substance5.pack(padx=5, pady=5)

dx=350;
dy=350;

canvas.create_window(x1+dx,y1+dy, window=substance5)


substance6 = Button(aminok,text='U', padx=100, pady=50)

substance6.config(width=5,height=5)
substance6.config(cursor='hand2')
substance6.config(bd=8, relief=RAISED)
substance6.config(bg='dark green', fg='white')
substance6.config(font=('helvetica', 20, 'italic'))
substance6.pack(padx=5, pady=5)

dx=350*2;
dy=350;

canvas.create_window(x1+dx,y1+dy, window=substance6)

########################################################################
# "Запуск" графического интерфейса

canvas.pack(expand=YES, fill=BOTH)
aminok.mainloop()


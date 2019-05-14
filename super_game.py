import tkinter
import sys
from tkinter import Tk
from tkinter import *
tkinter.NoDefaultRoot()
import subprocess
#from playsound import playsound
#####################################################################################################
# окно
root=Tk()
root.withdraw()
introduce= Toplevel(root)

introduce.geometry('1650x900')
introduce.title("Добро пожаловать!")

#winsound.PlaySound('song.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)

#PlaySound("Lindsey",SND_FILENAME)

############## закрытие
# def dest(event):
#     root.destroy()
#
# introduce.bind('<Destroy>',dest)

#########################################################################################

canvas = Canvas(introduce, width=1650, height=900, bg='green') # Холст. 0,0 - верхний левый угол.

#photo=PhotoImage(file="lena.gif")
#canvas.create_image(10, 10, image=photo, anchor=NW) # встроить изображение


#################################################################################
# заголовок
title=Label(introduce,text='Добро пожаловать! \n Что ботаем?')
title.config(bg='green',fg='white')
title.config(font=('helvetica', 40, 'bold italic'))

title_x=850
canvas.create_window(title_x,200, window=title)
###################################################################################
## кнопки

endx=title_x
endy=400
d=150

def struct():
    introduce.destroy()
    subprocess.run(['python','game_step2.py'])

def sokr():
    introduce.destroy()
    subprocess.run(['python','stroka_aminok.py'])

structure = Button(introduce,text='Строение аминокислот', padx=10, pady=30, command=struct)
structure.pack(padx=20, pady=20)
structure.config(cursor='hand2')
structure.config(bd=8, relief=RAISED)
structure.config(bg='dark green', fg='white')
structure.config(font=('helvetica', 20, 'underline italic'))


canvas.create_window(endx,endy, window=structure)

cycle = Button(introduce,text='Сокращения аминокислот', padx=95, pady=30,command=sokr)
cycle.pack(padx=20, pady=20)
cycle.config(cursor='hand2')
cycle.config(bd=8, relief=RAISED)
cycle.config(bg='dark green', fg='white')
cycle.config(font=('helvetica', 20, 'underline italic'))


canvas.create_window(endx,endy+d, window=cycle)

end = Button(introduce,text='Выход', padx=95, pady=30,command=sys.exit)
end.pack(padx=20, pady=20)
end.config(cursor='gumby')
end.config(bd=8, relief=RAISED)
end.config(bg='dark green', fg='white')
end.config(font=('helvetica', 20, 'underline italic'))


canvas.create_window(endx,endy+2*d, window=end)

############################################################################################


canvas.pack(expand=YES, fill=BOTH)

introduce.mainloop()


### Исправить баг с вываливанием при вводе неверного кол-ва 2 кнопка возвращения в меню 3 сделать статистику верных и неверных ответов в каждой из игр 4 Исправить пробллему с закрытием
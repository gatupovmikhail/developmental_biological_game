import tkinter
import sys
from tkinter import Tk
from tkinter import *
tkinter.NoDefaultRoot()

#####################################################################################################
# окно
introduce= Tk()

introduce.geometry('1650x900')
introduce.title("Добро пожаловать!")

#########################################################################################

canvas = Canvas(introduce, width=1650, height=900, bg='blue') # Холст. 0,0 - верхний левый угол.

#photo=PhotoImage(file="lena.gif")
#canvas.create_image(10, 10, image=photo, anchor=NW) # встроить изображение


#################################################################################
# заголовок
title=Label(introduce,text='Добро пожаловать! \n Что ботаем?')
title.config(bg='blue',fg='white')
title.config(font=('helvetica', 40, 'bold italic'))

title_x=850
canvas.create_window(title_x,200, window=title)
###################################################################################
## кнопки

endx=title_x
endy=400
d=150


structure = Button(introduce,text='Строение веществ', padx=10, pady=30)
structure.pack(padx=20, pady=20)
structure.config(cursor='hand2')
structure.config(bd=8, relief=RAISED)
structure.config(bg='dark green', fg='white')
structure.config(font=('helvetica', 20, 'underline italic'))


canvas.create_window(endx,endy, window=structure)

cycle = Button(introduce,text='Циклы', padx=95, pady=30)
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
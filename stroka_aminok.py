import tkinter
import sys
from tkinter import Tk
from tkinter import *
import random
import subprocess
#import super_game

aminoacids = [[1, 'Глицин', 'G', 'g.gif'], [2, 'Лейцин', 'L', 'l.gif'], [3, 'Тирозин', 'Y', 'y.gif'], [4, 'Серин', 'S', 's.gif'], [5, 'Глутаминовая_кислота', 'E', 'e.gif'], [6, 'Глутамин', 'Q', 'q.gif'], [7, 'Аспарагиновая_кислота', 'D', 'd.gif'], [8, 'Аспарагин', 'N', 'n.gif'], [9, 'Фенилаланин', 'F', 'f.gif'], [10, 'Аланин', 'A', 'a.gif'], [11, 'Лизин', 'K', 'k.gif'], [12, 'Аргинин', 'R', 'r.gif'], [13, 'Гистидин', 'H', 'h.gif'], [14, 'Цистеин', 'C', 'c.gif'], [15, 'Валин', 'V', 'v.gif'], [16, 'Пролин', 'P', 'p.gif'], [17, 'Триптофан', 'W', 'w.gif'], [18, 'Изолейцин', 'I', 'i.gif'], [19, 'Метионин', 'M', 'm.gif'], [20, 'Треонин', 'T', 't.gif']]

root=Tk()
root.withdraw()

def o_main_got():
    subprocess.Popen(['python','super_game.py'])
    root.destroy()


def main_func():


    winda = Toplevel(root)
    winda.geometry('1650x900')
    winda.title("Ботаем сокращения")




    global flag
    flag = 0
    #####
    canvas = Canvas(winda, width=1650, height=900, bg='green')

    menushka = Button(winda, command=o_main_got)
    menushka.config(cursor='hand2')
    menushka.config(text='Меню')
    menushka.config(bd=8, relief=RAISED)
    menushka.config(width=15, height=3)
    menushka.config(bg='dark green', fg='white')
    menushka.config(font=('helvetica', 20, 'italic'))
    menushka.pack(padx=5, pady=5)
    canvas.create_window(200, 650, window=menushka)

    ########################################### generation

    aminok_10 = [[] * 4] * 10

    l = []
    for i in range(20):
        l.append(i)

    l = random.sample(l, 10)

    for i in range(10):
        n = l[i]
        aminok_10[i] = aminoacids[n]

    stroka = ''
    for j in range(10):
        stroka = stroka + aminok_10[j][1] + '\n'
    ################################################## graphica
    name_aminok=Message(winda,text=stroka)
    name_aminok.config(bg='green', fg='white')
    name_aminok.config(font=('helvetica', 20, 'italic'))
    name_aminok.pack(padx=5, pady=5)
    canvas.create_window(200, 300, window=name_aminok)



    strokatext=StringVar()

    text_polen=Label(winda,text='Введите сокращения аминокислот через пробел:')
    text_polen.config(bg='green', fg='white')
    text_polen.config(font=('helvetica', 20, 'italic'))
    canvas.create_window(800, 720, window=text_polen)

    pole_name = Entry(winda, textvariable=strokatext)
    pole_name.config(width=40)
    pole_name.config(bg='dark green', fg='white')
    pole_name.config(font=('helvetica', 20, 'italic'))
    canvas.create_window(800, 800, window=pole_name)

    def com_knopki_dalee():
        vvod=strokatext.get()
        vvod=vvod.upper()
        attempt=vvod.split()


        global flag

        if not(len(attempt)==10):
            global flag
            flag = 1
            global attention
            attention = Message(winda, text='Вы ввели неверное \n количество аминокислот')
            attention.config(bg='dark green', fg='red')
            attention.config(font=('helvetica', 40, 'italic'))
            attention.pack(padx=5, pady=5)
            canvas.create_window(800, 300, window=attention)



        if (len(attempt) == 10):

            if (flag==1):

                attention.destroy()


            right_answers = 0
            wrong_answers = 0
            sokr = ''
            attempt_out = ''

            for j in range(10):
                sokr = sokr + aminok_10[j][2] + '\n'
                attempt_out = attempt_out + attempt[j] + '\n'

            system_answer = ''
            for j in range(10):
                if (attempt[j] == aminok_10[j][2]):
                    system_answer = system_answer + 'Верно' + '\n'
                    #global right_answers
                    right_answers+=1
                else:
                    system_answer = system_answer + 'Ошибка' + '\n'
                    #global wrong_answers
                    wrong_answers+=1

            pole_sokr=Message(winda,text='Верный ответ'+'\n'+sokr)
            pole_sokr.config(bg='green', fg='white')
            pole_sokr.config(font=('helvetica', 20, 'italic'))
            pole_sokr.pack(padx=5, pady=5)
            canvas.create_window(600,290,window=pole_sokr)

            pole_answers=Message(winda,text='Ваш ответ'+'\n'+attempt_out)
            pole_answers.config(bg='green', fg='white')
            pole_answers.config(font=('helvetica', 20, 'italic'))
            pole_answers.pack(padx=5, pady=5)
            canvas.create_window(800, 290, window=pole_answers)

            pole_prove = Message(winda, text='Верно ли?' + '\n' + system_answer)
            pole_prove.config(bg='green', fg='white')
            pole_prove.config(font=('helvetica', 20, 'italic'))
            pole_prove.pack(padx=5, pady=5)
            canvas.create_window(1000, 290, window=pole_prove)

            verno = Message(winda, text='Верно угадано:' + '\n' + '{}'.format(right_answers))
            verno.config(bg='green', fg='white')
            verno.config(font=('helvetica', 20, 'italic'))
            verno.pack(padx=5, pady=5)
            canvas.create_window(1200, 150, window=verno)

            neverno = Message(winda, text='Ошибок:' + '\n' + '{}'.format(wrong_answers))
            neverno.config(bg='green', fg='white')
            neverno.config(font=('helvetica', 20, 'italic'))
            neverno.pack(padx=5, pady=5)
            canvas.create_window(1400, 150, window=neverno)


            flag = 0

            dalee.destroy()

            cont = Button(winda, command=prodolzh)
            cont.config(cursor='hand2')
            cont.config(text='Еще раз')
            cont.config(bd=8, relief=RAISED)
            cont.config(width=15, height=3)
            cont.config(bg='dark green', fg='white')
            cont.config(font=('helvetica', 20, 'italic'))
            cont.pack(padx=5, pady=5)
            canvas.create_window(1500, 800, window=cont)

        canvas.pack(expand=YES, fill=BOTH)
        winda.mainloop()


    def com_knopki_dalee_enter(event):
        com_knopki_dalee()

    winda.bind('<Return>',com_knopki_dalee_enter)


    dalee = Button(winda, text='Далее', command=com_knopki_dalee)
    dalee.config(cursor='hand2')
    dalee.config(width=12, height=3)
    dalee.config(bd=8, relief=RAISED)
    dalee.config(bg='dark green', fg='white')
    dalee.config(font=('helvetica', 20, 'italic'))
    dalee.pack(padx=5, pady=5)
    canvas.create_window(1500, 800, window=dalee)

    stop = Button(winda, command=sys.exit)
    stop.config(cursor='hand2')
    stop.config(text='Закончить')
    stop.config(bd=8, relief=RAISED)
    stop.config(width=15, height=3)
    stop.config(bg='dark green', fg='white')
    stop.config(font=('helvetica', 20, 'italic'))
    stop.pack(padx=5, pady=5)
    canvas.create_window(200, 800, window=stop)

    def prodolzh():
        winda.destroy()
        main_func()

    canvas.pack(expand=YES, fill=BOTH)
    winda.mainloop()


main_func()



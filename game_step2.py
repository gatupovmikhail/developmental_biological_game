import random
import tkinter
import sys
from tkinter import Tk
from tkinter import *
import time
import subprocess
#####################################################################################################
# таблица аминокислот

####### initial data
aminoacids = [[1, 'Глицин', 'G', 'g.gif'], [2, 'Лейцин', 'L', 'l.gif'], [3, 'Тирозин', 'Y', 'y.gif'], [4, 'Серин', 'S', 's.gif'], [5, 'Глутаминовая_кислота', 'E', 'e.gif'], [6, 'Глутамин', 'Q', 'q.gif'], [7, 'Аспарагиновая_кислота', 'D', 'd.gif'], [8, 'Аспарагин', 'N', 'n.gif'], [9, 'Фенилаланин', 'F', 'f.gif'], [10, 'Аланин', 'A', 'a.gif'], [11, 'Лизин', 'K', 'k.gif'], [12, 'Аргинин', 'R', 'r.gif'], [13, 'Гистидин', 'H', 'h.gif'], [14, 'Цистеин', 'C', 'c.gif'], [15, 'Валин', 'V', 'v.gif'], [16, 'Пролин', 'P', 'p.gif'], [17, 'Триптофан', 'W', 'w.gif'], [18, 'Изолейцин', 'I', 'i.gif'], [19, 'Метионин', 'M', 'm.gif'], [20, 'Треонин', 'T', 't.gif']]

# инициализация корневого окна
root=Tk()
root.withdraw()






p=[]
for i in range(20):       # генерация списка из аминокислот в случайном порядке
    p.append(i)
p = random.sample(p, 20)


Raminoacids=[[]*4]*20
for i in range(20):
    n = p[i]
    Raminoacids[i]=aminoacids[n]



Nright_answers=0
Nwrong_answers=0
wrong_answers=[]
counter=0


# def dest(event):
#     root.destroy()

def finish_func():
    aminok = Toplevel(root)

    def ehe_raz():
        aminok.destroy()
        subprocess.run(['python', 'game_step2.py'])
    #aminok.bind('<Destroy>', dest)

    aminok.geometry('1650x900')
    aminok.title("Ваш результат")
    

    canvas = Canvas(aminok, width=1650, height=900, bg='green')

    title1 = Label(aminok, text='Количество верных ответов -  {}'.format(Nright_answers))
    title1.config(bg='green', fg='white')
    title1.config(font=('helvetica', 30, 'bold italic'))
    canvas.create_window(850, 100, window=title1)

    title2 = Label(aminok, text='Количество ошибок -  {}'.format(Nwrong_answers))
    title2.config(bg='green', fg='white')
    title2.config(font=('helvetica', 30, 'bold italic'))
    canvas.create_window(850, 200, window=title2)

    stop = Button(aminok, command=root.destroy)
    stop.config(cursor='hand2')
    stop.config(text='Закончить')
    stop.config(bd=8, relief=RAISED)
    stop.config(width=15, height=3)
    stop.config(bg='dark green', fg='white')
    stop.config(font=('helvetica', 20, 'italic'))
    stop.pack(padx=5, pady=5)
    canvas.create_window(700, 400, window=stop)

    cont = Button(aminok,command=ehe_raz)
    cont.config(cursor='hand2')
    cont.config(text='Еще раз')
    cont.config(bd=8, relief=RAISED)
    cont.config(width=15, height=3)
    cont.config(bg='dark green', fg='white')
    cont.config(font=('helvetica', 20, 'italic'))
    cont.pack(padx=5, pady=5)
    canvas.create_window(1050, 400, window=cont)

    canvas.pack(expand=YES, fill=BOTH)
    aminok.mainloop()

def o_main_got():
    subprocess.Popen(['python','super_game.py'])
    root.destroy()

def main_func():

    # алгоритм генерации случайных картинок аминокислот
    aminok_6 = [[] * 4] * 6



    l= []

    for i in range(20):
        if not(i==(Raminoacids[counter][0]-1)):
            l.append(i)


    l = random.sample(l, 6) #6 рандомных аминокислот в рандомных позициях


    refN = random.randint(0, 5)  # номер правильной из этих 6
    q=[]
    for i in range(6):
        if (i==refN):
            q.append(Raminoacids[counter][0]-1)
        if not(i==refN):
            q.append(l[i])


    aminok_6 = [[] * 4] * 6
    for i in range(6):
        n = q[i]
        aminok_6[i] = aminoacids[n]


    right_aminok = aminok_6[refN]
    #################################################


    ######################################################################################
    def podsvetka(refnum):
        if(refnum==0):
            substance1.config(bg='dark blue')
        elif (refnum==1):
            substance2.config(bg='dark blue')
        elif (refnum==2):
            substance3.config(bg='dark blue')
        elif (refnum==3):
            substance4.config(bg='dark blue')
        elif (refnum==4):
            substance5.config(bg='dark blue')
        elif (refnum==5):
            substance6.config(bg='dark blue')





    def com_knopki_dalee():
        global counter
        counter+=1
        if(counter<20):
            aminok.destroy()
            main_func()

        else:
            aminok.destroy()
            finish_func()

    def enter_dalee(event):
        global counter
        counter+=1
        if(counter<20):
            aminok.destroy()
            main_func()

        else:
            aminok.destroy()
            finish_func()



    def knopka_dalee():
        dalee = Button(aminok, text='Далее',command=com_knopki_dalee)
        dalee.config(cursor='hand2')
        dalee.config(width=12, height=3)
        dalee.config(bd=8, relief=RAISED)
        dalee.config(bg='dark green', fg='white')
        dalee.config(font=('helvetica', 20, 'italic'))
        dalee.pack(padx=5, pady=5)
        canvas.create_window(1500, 800, window=dalee)




    def bot1():
        if (aminok_6[0][0]==right_aminok[0]):
            substance1.config(bg='dark blue')
            title.config(text='Верно!')
            global Nright_answers
            Nright_answers += 1
        else:
            substance1.config(bg='red')
            title.config(text='Ошибочка...')
            global Nwrong_answers
            global wrong_answers
            Nwrong_answers+=1
            wrong_answers.append(aminok_6[0][0])
            podsvetka(refN)
        knopka_dalee()

    def ebot1(event):
        bot1()

    def bot2():
        if (aminok_6[1][0]==right_aminok[0]):
            substance2.config(bg='dark blue')
            title.config(text='Верно!')
            global Nright_answers
            Nright_answers+=1
        else:
            substance2.config(bg='red')
            title.config(text='Ошибочка...')
            global Nwrong_answers
            global wrong_answers
            Nwrong_answers+=1
            wrong_answers.append(aminok_6[1][0])
            podsvetka(refN)

        knopka_dalee()

    def ebot2(event):
        bot2()

    def bot3():
        if (aminok_6[2][0]==right_aminok[0]):
            substance3.config(bg='dark blue')
            title.config(text='Верно!')
            global Nright_answers
            Nright_answers+=1
        else:
            substance3.config(bg='red')
            title.config(text='Ошибочка...')
            global Nwrong_answers
            global wrong_answers
            Nwrong_answers+=1
            wrong_answers.append(aminok_6[2][0])
            podsvetka(refN)

        knopka_dalee()

    def ebot3(event):
        bot3()

    def bot4():
        if (aminok_6[3][0]==right_aminok[0]):
            substance4.config(bg='dark blue')
            title.config(text='Верно!')
            global Nright_answers
            Nright_answers+=1
        else:
            substance4.config(bg='red')
            title.config(text='Ошибочка...')
            global Nwrong_answers
            global wrong_answers
            Nwrong_answers+=1
            wrong_answers.append(aminok_6[3][0])
            podsvetka(refN)

        knopka_dalee()

    def ebot4(event):
        bot4()

    def bot5():
        if (aminok_6[4][0]==right_aminok[0]):
            substance5.config(bg='dark blue')
            title.config(text='Верно!')
            global Nright_answers
            Nright_answers+=1
        else:
            substance5.config(bg='red')
            title.config(text='Ошибочка...')
            global Nwrong_answers
            global wrong_answers
            Nwrong_answers+=1
            wrong_answers.append(aminok_6[4][0])
            podsvetka(refN)

        knopka_dalee()

    def ebot5(event):
        bot5()

    def bot6():
        if (aminok_6[5][0]==right_aminok[0]):
            substance6.config(bg='dark blue')
            title.config(text='Верно!')
            global Nright_answers
            Nright_answers+=1
        else:
            substance6.config(bg='red')
            title.config(text='Ошибочка...')
            global Nwrong_answers
            global wrong_answers
            Nwrong_answers+=1
            wrong_answers.append(aminok_6[5][0])
            podsvetka(refN)

        knopka_dalee()

    def ebot6(event):
        bot6()
    ######################################################################################
    # окно

    aminok= Toplevel(root)





    aminok.geometry('1650x900')
    aminok.title("Запоминание аминокислот")
    canvas = Canvas(aminok, width=1650, height=900, bg='green')
    # Холст. 0,0 - верхний левый угол.
    #####################################
    # ##################################################

    #################################
    title=Label(aminok,text='Выберите \n {}'.format(right_aminok[1]))
    title.config(bg='green',fg='white')
    title.config(font=('helvetica', 40, 'bold italic'))
    canvas.create_window(850,100, window=title)
    photo1=PhotoImage(file=aminok_6[0][3])
    photo2=PhotoImage(file=aminok_6[1][3])
    photo3=PhotoImage(file=aminok_6[2][3])
    photo4=PhotoImage(file=aminok_6[3][3])
    photo5=PhotoImage(file=aminok_6[4][3])
    photo6=PhotoImage(file=aminok_6[5][3])





    ##############################


    ### attempt
    #fr=Frame(can,width=100,height=100)
    #fr.pack()

    #canvas.create_window(350,500, window=fr)
    #
    # блок создания 6 кнопок



    substance1 = Button(aminok,command=bot1)

    substance1.config(image=photo1)
    substance1.config(cursor='hand2')
    substance1.config(bd=8, relief=RAISED)
    substance1.config(bg='dark green', fg='white')
    substance1.config(font=('helvetica', 20, 'italic'))
    substance1.pack(padx=5,pady=5)
    x1=500;
    y1=350;



    canvas.create_window(x1,y1, window=substance1)

    #substance2 = Button(aminok,text='L', padx=100, pady=50,wraplength=True)
    #substance2.config(width=5,height=5)
    substance2 = Button(aminok,image=photo2,command=bot2)
    substance2.config(cursor='hand2')
    substance2.config(bd=8, relief=RAISED)
    substance2.config(bg='dark green', fg='white')
    substance2.config(font=('helvetica', 20, 'italic'))
    substance2.pack(padx=5, pady=5)

    dx=350;
    dy=0;

    canvas.create_window(x1+dx,y1+dy, window=substance2)

    substance3 = Button(aminok,image=photo3,command=bot3)

    substance3.config(cursor='hand2')
    substance3.config(bd=8, relief=RAISED)
    substance3.config(bg='dark green', fg='white')
    substance3.config(font=('helvetica', 20, 'italic'))
    substance3.pack(padx=5, pady=5)

    dx=350*2;
    dy=0;

    canvas.create_window(x1+dx,y1+dy, window=substance3)

    substance4 = Button(aminok,image=photo4,command=bot4)

    substance4.config(cursor='hand2')
    substance4.config(bd=8, relief=RAISED)
    substance4.config(bg='dark green', fg='white')
    substance4.config(font=('helvetica', 20, 'italic'))
    substance4.pack(padx=5, pady=5)

    dx=0;
    dy=350;

    canvas.create_window(x1+dx,y1+dy, window=substance4)

    substance5 = Button(aminok,image=photo5,command=bot5)


    substance5.config(cursor='hand2')
    substance5.config(bd=8, relief=RAISED)
    substance5.config(bg='dark green', fg='white')
    substance5.config(font=('helvetica', 20, 'italic'))
    substance5.pack(padx=5, pady=5)

    dx=350;
    dy=350;

    canvas.create_window(x1+dx,y1+dy, window=substance5)


    substance6 = Button(aminok,image=photo6,command=bot6)

    substance6.config(cursor='hand2')
    substance6.config(bd=8, relief=RAISED)
    substance6.config(bg='dark green', fg='white')
    substance6.config(font=('helvetica', 20, 'italic'))
    substance6.pack(padx=5, pady=5)

    dx=350*2;
    dy=350;

    canvas.create_window(x1+dx,y1+dy, window=substance6)

    stop = Button(aminok,command=root.destroy)
    stop.config(cursor='hand2')
    stop.config(text='Стоп')
    stop.config(bd=8, relief=RAISED)
    stop.config(width=15, height=3)
    stop.config(bg='dark green', fg='white')
    stop.config(font=('helvetica', 20, 'italic'))
    stop.pack(padx=5, pady=5)
    canvas.create_window(150,100,window=stop)

    menushka = Button(aminok,command=o_main_got)
    menushka.config(cursor='hand2')
    menushka.config(text='Меню')
    menushka.config(bd=8, relief=RAISED)
    menushka.config(width=15, height=3)
    menushka.config(bg='dark green', fg='white')
    menushka.config(font=('helvetica', 20, 'italic'))
    menushka.pack(padx=5, pady=5)
    canvas.create_window(1450, 100, window=menushka)

    system_inform='Число \n попыток: {} \n \n Правильных \n ответов: {} \n \n Ошибок: {} \n \n Осталось: {}'.format(counter,Nright_answers,Nwrong_answers,20-counter)

    number_attemps = Message(aminok, text=system_inform)
    number_attemps.config(bg='green', fg='white')
    number_attemps.config(font=('helvetica', 20, 'italic'))
    number_attemps.pack(padx=5, pady=5)
    canvas.create_window(170, 700, window=number_attemps)

    aminok.bind('<Return>',enter_dalee)

    aminok.bind('1',ebot1)
    aminok.bind('2', ebot2)
    aminok.bind('3', ebot3)
    aminok.bind('4', ebot4)
    aminok.bind('5', ebot5)
    aminok.bind('6', ebot6)





    ########################################################################
    # "Запуск" графического интерфейса

    canvas.pack(expand=YES, fill=BOTH)
    aminok.mainloop()

main_func()
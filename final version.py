import tkinter as tk
from tkinter import ttk 
import pygame
from random import randint, shuffle
import pyperclip
#генерация кода модуля, чтобы среднее значение суммы попадало в диапазон между dmin и dmax
def password(dmin,dmax):
    letters_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    len(letters_list)
    s=0
    q=""
    qq=""
    for i in range(3):
        while True:
            a=randint(0, len(letters_list)-1)
            if (a+s)<dmax:
                s+=a
                q+=str(a)
                qq+=letters_list[a]
                break
    while True:
        a=randint(0, len(letters_list)-1)
        if ((a+s)>dmin) and ((a+s)<dmax):
            s+=a
            q+=str(a)
            qq+=letters_list[a]
            break
    return(qq)
#генерация ключа
def generate_password():
    global answer
    letters_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    blok1=""
    for i in range(5):
        blok1+=letters_list[randint(0, len(letters_list)-1)]
    blok1+="-"
    blok2=""
    for i in range(4):
        blok2+=letters_list[randint(0, len(letters_list)-1)]
    blok2+="-"
    print(777)
    blok3=password(30,120)
    answer = blok1+blok2+blok3
    canvas.itemconfig(pswd_canvas, text=answer)
# постановка музыки на паузу
def music_down():
    global music_down
    if music_down:
        music_down = False
        pygame.mixer.music.pause()
        return 0
    music_down = True
    pygame.mixer.music.unpause()

off_on_Music = True
root = tk.Tk()
root.title("GAME")
icon = tk.PhotoImage(file = "logo.png")
root.iconphoto(False, icon)
canvas = tk.Canvas(root, width=1920, height=1080)
canvas.pack()

image = tk.PhotoImage(file="game.png")
canvas.create_image(0, 0, anchor=tk.NW, image=image)

button_Music_down = ttk.Button(root, text="Поставить музыку на паузу", command=music_down)
button_Music_down_canvas = canvas.create_window(380, 700, anchor="nw", window=button_Music_down)

button_pswd = ttk.Button(root, text="Сгенерировать пароль", command=generate_password)
button_pswd_canvas = canvas.create_window(600, 100, anchor="nw", window=button_pswd)

pswd_canvas = canvas.create_text(680, 50, text="Генерация ключа", fill="blue", font=('Arial 30 bold'))



canvas.pack(fill="both", expand=True)

# Play music
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)

root.mainloop()

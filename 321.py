import tkinter as tk
from tkinter import ttk 
import pygame
from random import randint, shuffle
import pyperclip


def generate_password():
    global answer
    answer = ""
    for _ in range(3):
        letters = [chr(randint(65, 90)) for _ in range(3)]
        num = str(randint(0, 9))
        answer_lst = letters.copy()
        answer_lst.append(num)
        shuffle(answer_lst)
        answer_str = "".join(answer_lst)
        answer += answer_str + "-"
    answer = answer[:-1]
    canvas.itemconfig(pswd_canvas, text=answer)


def copy_password():
    pyperclip.copy(answer)
    label = tk.Label(root, text="Вы скопировали пароль!", font=("Arial", 25), fg="blue")
    label_window = canvas.create_window(860, 280, window=label)
    root.after(3000, lambda: canvas.delete(label_window))#


def OffMusic():
    global off_on_Music
    if off_on_Music:
        off_on_Music = False
        pygame.mixer.music.pause()
        return 0
    off_on_Music = True
    pygame.mixer.music.unpause()


answer = ""
off_on_Music = True
root = tk.Tk()
root.title("GAME")
icon = tk.PhotoImage(file = "logo.png")
root.iconphoto(False, icon)
canvas = tk.Canvas(root, width=1920, height=1080)
canvas.pack()

image = tk.PhotoImage(file="game.png")
canvas.create_image(0, 0, anchor=tk.NW, image=image)

# button for off/on music
button_OffMusic = ttk.Button(root, text="Поставить музыку на паузу", command=OffMusic)
button_OffMusic_canvas = canvas.create_window(50, 50, anchor="nw", window=button_OffMusic)

# button for generate password
button_pswd = ttk.Button(root, text="Сгенерировать пароль", command=generate_password)
button_pswd_canvas = canvas.create_window(865, 200, anchor="nw", window=button_pswd)

# password output
pswd_canvas = canvas.create_text(860, 150, text="Генерация ключа", fill="white", font=('Arial 30 bold'))

# button for copy password
button_copy = ttk.Button(root, text="скопировать пароль", command=copy_password)
button_copy_canvas = canvas.create_window(700, 200, anchor="nw", window=button_copy)

# copy output
copy_canvas = canvas.create_text(730, 250, text="", fill="white", font=('Arial 30 bold'))


canvas.pack(fill="both", expand=True)

# Play music
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("4.mp3")
pygame.mixer.music.play(-1)


root.mainloop()

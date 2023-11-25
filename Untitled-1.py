from tkinter import *
from tkinter import ttk     # подключаем пакет ttk
def click_button():
    clicks = 0
    clicks = clicks+1
    # изменяем текст на кнопке
    btn["text"] = f"Clicks {clicks}"   
    print("+1")


root = Tk() 
root.title("GAME")
icon = PhotoImage(file = "logo.png")
root.iconphoto(False, icon)


btn = ttk.Button(text="Click Me", command=click_button)

btn.pack()
btn2 = ttk.Button(text="Button2")
btn2.pack()

root.state('zoomed')
root.mainloop()
'''from tkinter import *
 
window = Tk()     # создаем корневой объект - окно
#root.title("Приложение на Tkinter")     # устанавливаем заголовок окна
#root.geometry("300x250")    # устанавливаем размеры окна
bg_img = PhotoImage(file='game.png')
label =Label(window, image=bg_img)

#label = Label(text="Hello METANIT.COM") # создаем текстовую метку
label.pack()    # размещаем метку в окне
window.mainloop()'''
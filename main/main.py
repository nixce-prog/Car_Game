from tkinter import *
from PIL import Image, ImageTk
from Player import Player


def root1():
    root.destroy()

    root1 = Tk()
    root1.title('Car Game')
    root1.geometry('800x450')
    root1.resizable(False, False)

    bg_image = Image.open(r'C:\Users\User\Desktop\Новая папка (9)\bg (1).png')
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = Label(root1, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    playbtn = Button(root1, text='Играть', font=('italic', 15), width=15, height=4)
    playbtn.place(x=600, y=320)
    storebtn = Button(root1, text='Магазин', font=('italic', 15), width=13, height=2)
    storebtn.place(x=621, y=250)
    statsbtn = Button(root1, text='Статистика', font=('italic', 15), width=12, height=2)
    statsbtn.place(x=25, y=366)

    root1.mainloop()


def translate():
    log = login.get()
    pas = password.get()
    player = Player(log, pas)
    if player.accaunt == 1:
        checkbtn.destroy()
        nxbtn = Button(root, text='Продолжить', font=('Italic', 12), command=root1, bg='green',
        fg='black', activebackground='green', activeforeground='white')
        nxbtn.place(x=360, y=310)
    elif player.accaunt == 2:
        reglb = Label(root, text='Аккаунт был создан!', font=('italic', 14), bg='black', fg='white')
        reglb.place(x=15, y=20)
        nxbtn = Button(root, text='Продолжить', font=('Italic', 12), command=root1, bg='green',
                                   fg='black', activebackground='green', activeforeground='white')
        nxbtn.place(x=360, y=310)


if __name__ == "__main__":
    root = Tk()
    root.title('Car_Game')
    root.geometry('800x450')
    root.resizable(False, False)
    root['bg'] = 'black'

    image_path = r"login.png"
    tk_image = PhotoImage(file=image_path)

    image_label = Label(root, image=tk_image)
    image_label.pack()

    login = Entry(root, width=30)
    login.place(x=250, y=220)

    password = Entry(root, width=30)
    password.place(x=250, y=260)

    checkbtn = Button(root, text='Проверить', font=('Italic', 12), command=translate, bg='grey',
                      fg='black', activebackground='green', activeforeground='white')
    checkbtn.place(x=360, y=310)

    lb_login = Label(root, text='Логин:', font=('Italic', 12), bg='black', fg='white')
    lb_login.place(x=190, y=215)
    lb_password = Label(root, text='Пароль:', font=('Italic', 12), bg='black', fg='white')
    lb_password.place(x=180, y=257)

    root.mainloop()

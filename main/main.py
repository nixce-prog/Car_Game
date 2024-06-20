from tkinter import *
import os.path
from PIL import Image, ImageTk
import json

class Player():
    default = [("money", 0, int), ("win", 0, str), ("password", "0000", str), ("bad", 0, int)]
    info_d = {x[0]: x[2](x[1]) for x in default}

    def __init__(self, login, password):
        info = {}
        if os.path.isfile("profile.txt"):
            with open("profile.txt", "r+") as f:
                s = json.load(f)
                if login in s:
                    if s[login]["password"] == password:
                        if len(s[login]) == len(Player.default) + 1:
                            info = s[login]
                        else:
                            for x in Player.default:
                                if x[0] not in s[login]:
                                    s[login][x[0]] = x[2](x[1])
                            info = s[login]
                            f.seek(0)
                            f.truncate()
                            json.dump(s, f)
                        checkbtn.destroy()
                        nxbtn = Button(root, text='Продолжить', font=('Italic', 12), command=root1, bg='green',
                                       fg='black', activebackground='green', activeforeground='white')
                        nxbtn.place(x=360, y=310)
                else:
                    f.seek(0)
                    f.truncate()
                    info = Player.info_d
                    info["password"] = password
                    s[login] = info
                    json.dump(s, f)
                    reglb = Label(root, text='Аккаунт был создан!', font=('italic', 14), bg='black', fg='white')
                    reglb.place(x=15, y=20)
                    nxbtn = Button(root, text='Продолжить', font=('Italic', 12), command=root1, bg='green',
                                   fg='black', activebackground='green', activeforeground='white')
                    nxbtn.place(x=360, y=310)
        else:
            with open("profile.txt", "w+") as f:
                info = Player.info_d
                info["password"] = password
                json.dump({login: info}, f)

        g = {x[0]: x[2] for x in Player.default}
        self.info = {x[0]: g[x[0]](info.get(x[0], x[1])) for x in info.items()}


def root1():
    root.destroy()

    root1 = Tk()
    root1.title('Car Game')
    root1.geometry('800x450')
    root1.resizable(False, False)

    bg_image = Image.open('bg.png')
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
    Player(log, pas)


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
from tkinter import *
from tkinter import messagebox  
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
                try:
                    s = json.load(f)
                except json.JSONDecodeError:
                    s = {}  
                    f.seek(0) 
                    f.truncate()

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
                        self.account_created = True
                else:
                    f.seek(0)
                    f.truncate()
                    info = Player.info_d
                    info["password"] = password
                    s[login] = info
                    json.dump(s, f)
                    self.account_created = True
        else:
            with open("profile.txt", "w+") as f:
                info = Player.info_d
                info["password"] = password
                json.dump({login: info}, f)
                self.account_created = True

        g = {x[0]: x[2] for x in Player.default}
        self.info = {x[0]: g[x[0]](info.get(x[0], x[1])) for x in info.items()}
        self.info["login"] = login



def root1():
    global root, game_window
    root.destroy()

    game_window = Tk()
    game_window.title('Car Game')
    game_window.geometry('800x450')
    game_window.resizable(False, False)

    bg_image = Image.open('bg.png')
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = Label(game_window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    playbtn = Button(game_window, text='Играть', font=('italic', 15), width=15, height=4)
    playbtn.place(x=600, y=320)
    storebtn = Button(game_window, text='Магазин', font=('italic', 15), width=13, height=2)
    storebtn.place(x=621, y=250)
    statsbtn = Button(game_window, text='Статистика', font=('italic', 15), width=12, height=2, command=show_statistics)
    statsbtn.place(x=25, y=366)

    game_window.mainloop()


def translate():
    global login_value, password_value, player
    login_value = login.get()
    password_value = password.get()
    player = Player(login_value, password_value)
    if player.account_created:
        reglb = Label(root, text='Аккаунт был создан!', font=('italic', 14), bg='black', fg='white')
        reglb.place(x=15, y=20)
        nxbtn = Button(root, text='Продолжить', font=('Italic', 12), command=root1, bg='green',
                       fg='black', activebackground='green', activeforeground='white')
        nxbtn.place(x=360, y=310)
    else:
        messagebox.showinfo('Ошибка', 'Неправильный логин или пароль.')


def show_statistics():
    global player
    try:
        with open("profile.txt", "r") as f:
            s = json.load(f)
            if player.info["login"] in s: 
                player_stats = s[player.info["login"]]
                stats_text = f"Статистика игрока {player.info['login']}:\n"
                stats_text += f"Пароль: {player.info['password']}\n"
                for key, value in player_stats.items():
                    if key != 'password': 
                        stats_text += f"{key}: {value}\n"
                messagebox.showinfo('Статистика игрока', stats_text)
            else:
                messagebox.showinfo('Ошибка', 'Игрок не найден.')
    except FileNotFoundError:
        messagebox.showinfo('Ошибка', 'Файл профиля не найден.')


if __name__ == "__main__":
    root = Tk()
    root.title('Car_Game')
    root.geometry('800x450')
    root['bg'] = 'black'

    image_path = r"login.gif"
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

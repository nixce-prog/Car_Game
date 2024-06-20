from tkinter import *
from PIL import Image, ImageTk
from Player import Player
player = None

def buy(car):
    global player
    player.buy(car)



def root1():
    root1 = Toplevel()
    root1.title('Car Game')
    root1.geometry('800x450')
    root1.resizable(False, False)


    def r_destr():
        root1.destroy()
        roots()




    def r2_destr():
        root1.destroy()
        store()


    bg_image = Image.open(r'bg.png')
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = Label(root1, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    playbtn = Button(root1, text='Играть', font=('italic', 15), width=15, height=4)
    playbtn.place(x=600, y=320)
    storebtn = Button(root1, text='Магазин', font=('italic', 15),command=r2_destr, width=13, height=2)
    storebtn.place(x=621, y=250)
    statsbtn = Button(root1, text='Статистика', font=('italic', 15),command=r_destr, width=12, height=2)
    statsbtn.place(x=25, y=366)

    root1.mainloop()


def store():
    store = Toplevel()
    store.title('Car Shop')
    store.geometry('800x450')
    store['bg'] = 'grey'

    def rdestr():
        store.destroy()
        root1()

    lb_bg1 = Label(store, bg='black', width=34, height=20)
    lb_bg1.place(x=45, y=35)
    lb_bg2 = Label(store, bg='black', width=34, height=20)
    lb_bg2.place(x=350, y=35)

    bg_image = Image.open(r'dodge.png')
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = Label(store, image=bg_photo, width=170)
    bg_label.place(x=80, y=60)

    car_pho2 = Image.open(r'lambo.png')
    car_photo2 = ImageTk.PhotoImage(car_pho2)
    Lb = Label(store, image=car_photo2, width=170, height=130)
    Lb.place(x=380, y=60)

    buydg = Button(store, text='Купить', bg='yellow', fg='green', activebackground='red', activeforeground='white',
                   width=9,command=lambda: buy("volvo"))
    buydg.place(x=180, y=280)
    buylamb = Button(store, text='Купить', bg='yellow', fg='green', activebackground='red', activeforeground='white',
                     width=9)
    buylamb.place(x=480, y=280)
    back = Button(store, text='Назад', command=rdestr, width=10, height=2)
    back.place(x=45, y=380)
    store.mainloop()


def roots():
    global player

    root2 = Toplevel()
    root2.title('Car Game')
    root2.geometry('800x450')
    root2.resizable(False, False)

    def r1_dest():
        root2.destroy()
        root1()

    bg_image = Image.open(r'bg.png')
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = Label(root2, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    lb_money = Label(root2, text=str(player.info['money']),font=('italic', 15))
    lb_money.place(x=690,y=30)
    lb_money1 = Label(root2, text="Деньга",font=('italic', 15))
    lb_money1.place(x=590,y=30)
    lb_win = Label(root2, text=str(player.info['win']),font=('italic', 15))
    lb_win.place(x=690,y=60)
    lb_win1 = Label(root2, text="Победы",font=('italic', 15))
    lb_win1.place(x=590,y=60)
    lb_bad = Label(root2, text=str(player.info['bad']),font=('italic', 15))
    lb_bad.place(x=690,y=90)
    lb_bad1 = Label(root2, text="Лузы",font=('italic', 15))
    lb_bad1.place(x=590,y=90)

    bkbtn = Button(root2, text='Назад',font=('italic', 15), command=r1_dest)
    bkbtn.place(x=30,y=290)



    root2.mainloop()

def translate():
    global player
    log = login.get()
    pas = password.get()
    player = Player(log, pas)
    if player.accaunt == 1:
        checkbtn.destroy()
        nxbtn = Button(root, text='Продолжить', font=('Italic', 12), command=root_dest, bg='green',
        fg='black', activebackground='green', activeforeground='white')# dest
        nxbtn.place(x=360, y=310)
    elif player.accaunt == 2:
        reglb = Label(root, text='Аккаунт был создан!', font=('italic', 14), bg='black', fg='white')
        reglb.place(x=15, y=20)
        nxbtn = Button(root, text='Продолжить', font=('Italic', 12), command=root_dest, bg='green',
                                   fg='black', activebackground='green', activeforeground='white')# dest
        nxbtn.place(x=360, y=310)


if __name__ == "__main__":
    root = Tk()
    root.title('Car_Game')
    root.geometry('800x450')
    root.resizable(False, False)
    root['bg'] = 'black'


    def root_dest():
        root.destroy()
        root1()

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

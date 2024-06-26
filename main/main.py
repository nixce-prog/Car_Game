from tkinter import *
from PIL import Image, ImageTk
from Player import Player
from functools import partial
import pygame
import random


player = None






def root1():
    menu = Tk()
    menu.title('Car Game')
    menu.geometry('800x450')
    menu.resizable(False, False)


    def game():
        global player
        menu.destroy()
        pygame.init()

        window = pygame.display.set_mode((1200, 700))
        Clok = pygame.time.Clock()

        image = pygame.image.load("dggame.png")
        image = pygame.transform.scale(image, (150, 50))
        image2 = pygame.image.load("road.png")
        image2 = pygame.transform.scale(image2, (1200, 700))

        class sprite(object):

            sprite_list = {}

            def __init__(self, speed, size, image, x, y, max_speed, hard) -> None:
                self.speed = speed
                self.size = size
                self.image = pygame.transform.scale(image, size)
                self.image_old = image
                self.x = x
                self.y = y
                self.max_speed = max_speed
                self.max_speed_old = max_speed
                self.hard = hard

                sprite.sprite_list[self] = [self.image, [x, y]]

            def obnow():
                for x in sprite.sprite_list:
                    x.image = pygame.transform.scale(x.image_old, x.size)
                    sprite.sprite_list[x] = [x.image, [x.x, x.y]]

            def exit():
                sprite.sprite_list = {}

        class player1(sprite):
            pass

        interesting = 100

        s = player1(0, [150, 100], image, 100, 160, 220, 1)
        g = sprite(0, (150, 100), image, 100, 250, 230, random.randrange(int(interesting / 2), interesting) / 100)
        g = sprite(0, (150, 100), image, 100, 350, 222, random.randrange(int(interesting / 2), interesting) / 100)
        g = sprite(0, (150, 100), image, 100, 450, 230, random.randrange(int(interesting / 2), interesting) / 100)

        g_r = random.randrange(200) / 100

        x_a = 0

        runing = True

        race_time = (60) / 2
        Fps = 60
        t = 0

        while runing:
            t += 1
            keys = pygame.key.get_pressed()

            x_a += s.speed
            if x_a >= 1200:
                x_a = 0

            for x in sprite.sprite_list:
                if x != s:
                    x.x += x.speed - s.speed
                    if x.speed < x.max_speed / 2:
                        x.speed += x.max_speed / race_time / Fps * x.hard

                else:
                    if not keys[pygame.K_d]:
                        if x.speed > 0:
                            x.speed *= 0.995
                    else:
                        if s.speed < s.max_speed / 2:
                            s.speed += s.max_speed / race_time / Fps

            sprite.obnow()

            window.blit(image2, (0 - x_a, 0))
            window.blit(image2, (1200 - x_a, 0))

            window.blits([*sprite.sprite_list.values()])

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runing = False
                    pygame.quit()
            Clok.tick(Fps)
            if t // 60 >= race_time:
                p = [x[1] for x in sorted({x.x: x for x in sprite.sprite_list}.items())]
                f = p.index(s)
                player.info['money'] += f * interesting
                player.info['win'] += 1
                player.save()
                runing = False
                pygame.quit()

                finish = Tk()
                finish.title('Finish')
                finish.geometry('300x300')

                def finisher():
                    finish.destroy()
                    root1()

                lb = Label(finish, text=f * interesting, font=('italic', 15), bg='white', fg='black')
                lb.place(x=135, y=60)

                btn = Button(finish, text='Назад',command=finisher, font=('italic', 10))
                btn.place(x=160, y=100)

                finish.mainloop()

                return f * interesting

    def r_destr():
        menu.destroy()
        roots()


    def r2_destr():
        menu.destroy()
        store()


    bg_image = Image.open(r'bg.png')
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = Label(menu, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    playbtn = Button(menu, text='Играть', font=('italic', 15),command=game, width=15, height=4)
    playbtn.place(x=600, y=320)
    storebtn = Button(menu, text='Магазин', font=('italic', 15),command=r2_destr, width=13, height=2)
    storebtn.place(x=621, y=250)
    statsbtn = Button(menu, text='Статистика', font=('italic', 15),command=r_destr, width=12, height=2)
    statsbtn.place(x=25, y=366)

    menu.mainloop()


def store():

    a = {}

    def buy(car):
        global player
        player.buy(car)
        if player.info['car'][car] == True:
            a[car].destroy()
        else:
            print('Сударь, идите пожалуйста на работу')


    store = Tk()
    store.title('Car Shop')
    store.geometry('800x450')
    store.resizable(False, False)
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
    if player.info['car']['Dodge'] == False:
        buydg = Button(store, text='Бесплатно', bg='yellow', fg='green', activebackground='red', activeforeground='white',
                       width=9, command=partial(buy, "Dodge"))
        buydg.place(x=180, y=280)
        a["Dodge"] = buydg
    if player.info['car']['Lamborgini'] == False:
        buylamb = Button(store, text='1000ввввввввввввввввв', bg='yellow', fg='green', activebackground='red',activeforeground='white',
                         width=9, command=partial(buy, "Lamborgini"))
        buylamb.place(x=480, y=280)
        a["Lamborgini"] = buylamb


    car_pho2 = Image.open(r'lambo.png')
    car_photo2 = ImageTk.PhotoImage(car_pho2)
    Lb = Label(store, image=car_photo2, width=170, height=130)
    Lb.place(x=380, y=60)

    back = Button(store, text='Назад', command=rdestr, width=10, height=2)
    back.place(x=45, y=380)


    store.mainloop()


def roots():
    global player

    root2 = Tk()
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
    zapr = [" ",",","-","."]
    if len(log)  >= 4 and len(pas) >= 4 and log != 'system' and all([log.count(x) < 4 for x in zapr]) and all([pas.count(x) < 4 for x in zapr]):
        player = Player(log, pas)
        if player.accaunt == 1:
            checkbtn.destroy()
            nxbtn = Button(root, text='Продолжить', font=('Italic', 12), command=root_dest, bg='green',
            fg='black', activebackground='green', activeforeground='white')
            nxbtn.place(x=360, y=310)
        elif player.accaunt == 2:
            reglb = Label(root, text='Аккаунт был создан!', font=('italic', 14), bg='black', fg='white')
            reglb.place(x=15, y=20)
            nxbtn = Button(root, text='Продолжить', font=('Italic', 12), command=root_dest, bg='green',
                                       fg='black', activebackground='green', activeforeground='white')
            nxbtn.place(x=360, y=310)
    else:
        print('Введите корректный логин (от 4 символов)')

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

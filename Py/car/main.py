from tkinter import *
import os.path

class Player():

    defolt = [("money",0,int),("win",0,str),("pasword",0000,str),("bad",0,int)]
    info_d = {x[0]:x[2](x[1]) for x in defolt}

    def __init__(self,login,password):
        info = {}
        if os.path.isfile("profile.txt"):
            with open("profile.txt","r+") as f:
                    s = eval(f.read())
                    if type(s) == dict:
                        if login in s:
                            if str(s[login]["pasword"]) == password:
                                if len(s[login]) == len(Player.defolt)+1:
                                    info = s[login]
                                    
                                else:
                                    for x in Player.defolt:
                                        if not (x[0] in s[login]):
                                            s[login][x[0]] = x[2](x[1])
                                    info = s[login]
                                    f.seek(0)
                                    f.truncate()
                                    f.write(str(s))
                                checkbtn.destroy()
                                nxbtn = Button(root,text='Продолжить',font=('Italic', 12),command=root1,bg='green',fg='black',activebackground='green',activeforeground='white')
                                nxbtn.place(x=360, y=310)
                        else:
                            f.seek(0)
                            f.truncate()
                            info = Player.info_d
                            info["pasword"] = password
                            s[login] = info
                            f.write(str(s))
                            reglb = Label(root, text='Аккаунт был создан!', font=('italic', 14), bg='black', fg='white')
                            reglb.place(x=15,y=20)
                            nxbtn = Button(root, text='Продолжить', font=('Italic', 12), command=root1, bg='green', fg='black',activebackground='green', activeforeground='white')
                            nxbtn.place(x=360, y=310)
        else:
            with open("profile.txt","w+") as f:
                f.seek(0)
                f.truncate()
                info = Player.info_d
                info["pasword"] = password
                f.write(str({login:info}))
        g = {x[0]:x[2] for x in Player.defolt}
        self.info = {x[0]:g[x[0]](x[1]) for x in info.items()}



root = Tk()
root.title('Car_Game')
root.geometry('800x450')
root['bg'] = 'black'



def root1():

    root.destroy()

    root1 = Tk()
    root1.title('Car_Game')
    root1.geometry('800x450')
    root1['bg'] = 'black'
    root1.mainloop()

def tranlate():
    log = login.get()
    pas = password.get()
    Player(log,pas)
    


            

if __name__ == "__main__":
    image_path = r"C:\Users\User\Desktop\Новая папка (7)\code\login.gif"
    tk_image = PhotoImage(file=image_path)

    image_label = Label(root, image=tk_image)
    image_label.pack()

    login = Entry(root,
                width=30
                )
    login.place(x=250,y=220)

    password = Entry(root,
                width=30
                )
    password.place(x=250,y=260)

    checkbtn = Button(root,
                    text='Проверить',
                    font=('Italic', 12),
                    command=tranlate,
                    bg='grey',
                    fg='black',
                    activebackground='green',
                    activeforeground='white'
                    )
    checkbtn.place(x=360, y=310)

    lb_login = Label(root, text='Логин:', font=('Italic', 12), bg='black', fg='white')
    lb_login.place(x=190,y=215)
    lb_password = Label(root, text='Пароль:', font=('Italic', 12), bg='black', fg='white')
    lb_password.place(x=180,y=257)

    root.mainloop()

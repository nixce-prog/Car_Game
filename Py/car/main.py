from tkinter import *
import os.path

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
    save(log,pas)
    

def save(login,password):

    if os.path.isfile("profile.txt"):
        with open("profile.txt","r+") as f:
                s = eval(f.read())
                if type(s) == dict:
                    if login in s:
                        if str(s[login]["pasword"]) == password:
                            root1()
                    else:
                        f.seek(0)
                        f.truncate()
                        s[login] = {"pasword":str(password)}
                        f.write(str(s))
    else:
        with open("profile.txt","w+") as f:
            f.seek(0)
            f.truncate()
            f.write(str({login:{"pasword":str(password)}}))
            

image_path = r"login.gif"
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

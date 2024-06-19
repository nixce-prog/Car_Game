from tkinter import *

root = Tk()
root.title('Car_Game')
root.geometry('800x450')
root['bg'] = 'black'

def root1():


image_path = r"C:\Users\mcajk\OneDrive\Документы\Py\car\login.gif"
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

accept = Button(root,
                text='Принять',
                font=('Italic', 12),
                command= ,
                bg='grey',
                fg='black',
                activebackground='green',
                activeforeground='white'
                )
accept.place(x=360, y=310)

lb_login = Label(root, text='Логин:', font=('Italic', 12), bg='black', fg='white')
lb_login.place(x=190,y=215)
lb_password = Label(root, text='Пароль:', font=('Italic', 12), bg='black', fg='white')
lb_password.place(x=180,y=257)

root.mainloop()

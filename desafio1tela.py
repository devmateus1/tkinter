from tkinter import *

i = Tk()
i.title("Programa Financeiro")
i.geometry('980x720+250+30')

lb1 = Label(i, text="Login", bg="yellow")
#componente .grid serve tambem para posicionar utilizano indicativo de linha (row) coluna (column).
lb1.place(x=1300, y=200)

lb2 = Label(i, text="Senha", bg="red")
lb2.place(x=1300, y=280)

ed1 = Entry(i)
ed1.place(x=1300, y=300, width=300)

ed2 = Entry(i)
ed2.place(x=1300, y=220, width=300)

bt1 = Button(i, text="Login")
bt1.place(x=900, y=800,width=50)

i.mainloop()
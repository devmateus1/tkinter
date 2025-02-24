from tkinter import *

def bt_soma():
    num1 = int(ed1.get())
    num2 = int(ed2.get())

    lb["text"] = num1 + num2
    lb = Label(i, text="0")
    lb.place(x=230,y=230)
    
def bt_subtracao(): 
    num1 = int(ed1.get())
    num2 = int(ed2.get())

    lb["text"] = num1 - num2
   
def bt_multiplicacao(): 
    num1 = int(ed1.get())
    num2 = int(ed2.get())

    lb["text"] = num1 * num2
    
    

def bt_divisao(): 
    num1 = int(ed1.get())
    num2 = int(ed2.get())

    lb["text"] = num1 / num2
    

i = Tk()
i.title("Programa Financeiro")
i.geometry('980x720+250+30')

lb = Label(i, text="0")
lb.place(x=230,y=230)

bt = Button(i, width="20", text='soma', command=bt_soma)
bt.place(x=250,y=200)

bt = Button(i, width="20", text='subtração', command=bt_subtracao)
bt.place(x=400,y=200)

bt = Button(i, width="20", text='multiplicação', command=bt_multiplicacao)
bt.place(x=600,y=200)    

bt = Button(i, width="20", text='divisao', command=bt_divisao)
bt.place(x=800,y=200)    

ed1 = Entry(i)
ed1.place(x=230, y=150)

ed2 = Entry(i)
ed2.place(x=230, y=180)

i.mainloop()
from tkinter import *

i = Tk()
i.title("Programa Financeiro")
i.geometry('980x720+250+30')

lb1 = Label(i, text="Label 1 ", bg="yellow" )
lb1.place(x=230,y=200)

lb2 = Label(i, text="Label 2 ", bg="red" )
lb2.place(x=230,y=200)

lb3 = Label(i, text="Label 3 ", bg="green" )
lb3.place(x=230,y=200)

lb4 = Label(i, text="Label 4 ", bg="blue" )
lb4.place(x=230,y=200)

#codigo abaixo posiciona cada lable em lugares diferentes 
#apos testar comente a linha do lb1 ate o lb4

lb1.pack(side= LEFT)
lb2.pack(side="left")
lb3.pack(anchor="w") # sempre que nao utilizo a opção side, ele sempre sera topo.
#lb4.pack(anchor="w") # sempre que nao utilizo a opção side, ele sempre sera topo.
#lb4.pack(side=BOTTOM, anchor= "sw")

lb4.pack( anchor= "e")

i.mainloop()
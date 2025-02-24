from tkinter import *

#criando uma função para clique no botao
def bt_click():
    # o label que usar propriedade text recebera a mensagem "Trocou o texto"
    lb["text"] = "Trocou o texto"
    
    #esse print abaixo exibe o texto na tela do console 
    print("O botão foi cilcado")

def bt_clickar():
    #esse print exibe o texto digitado na caixa de texto e exibe na lable da tela 
    print(ed.get())
    lb=["text"]=ed.get()

    # o i de instanciar recebe o objeto tk 
    i = Tk()

    #gerar titulo na janela 
    i.title('Programa Financeiro')
    i.geometry('980x720+250+30')
    i=["bg"]="green"

    #i.wn_iconbitmap('icone.ico')

    lb = Label(i, text='Nome do usuario')
    lb.place(x=100,y=100)

    bt = Button(i, width="20", text='ok', command=bt_click)
    bt.place(x=230,y=100)

    #o codigo abaixo cria um botao e posiciona abaixo do botao ok
    bt = Button(i, width="20", text='capturar',command=bt_clickar)
    bt.place(x=230,y=190)

    #cria a caixa de texto 
    ed = Entry(i)
    ed.place(x=230,y=150)

    i.mainloop()
#comando abaixo importa tudo da biblioteca que é necessaria
#para a criação de telas. (ASTERISCO significa tudo )
from tkinter import *

#i (instanciar ) recebe o objeto tk
i = Tk()

#gerar titulo da janela
i.title('Program Financeiro')

#propriedade que altera o tamanho da janela 
#(980x920) e distancia da direita e topo da tela 
#(250x30)
i.geometry('980x720+250+30')

#propriedades graficas , cor de fundo da tela (bg) ou (background)
#não pode passar o i com ponto DEVE ser i[]
i['bg'] = "yellow"

#Cria o icone na janela, voce deve ter a imagem no mesmo local do codigo.
#i.wn_iconbitmap('icone.ico')

#crie label e posiciona (place) ele em relação a tela 
lb = Label(i,text='Nome do usuario')
lb.place(x=100,y=100)

#cria um botão que posiciona (place) ele em relação a lable.
bt = Button(i, width='20',text='ok')
bt.place(x=230,y=100)

#gera a janela grafica 
i.mainloop()


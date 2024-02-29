#CREATOR
#GitHub - > TonnyThe2nd
#Instagram - > @web_4ntonio
#E-mail - > antoniomarcos3577@gmail.com
#Linkedn - >    www.linkedin.com/in/antonio-marcos-sousa-de-oliveira-25b902272

from deep_translator import GoogleTranslator
import gtts
from tkinter import *
from tkinter import ttk
#FUNÇÃO PARA TRADUZIR
def texto_translate():
    texto = caixa_traduzir.get()
    len_traduzir = lingua_traduzir.get()
    len_traduzida = lingua_traduzida.get()
    traducao_comando = GoogleTranslator(source=len_traduzir, target=len_traduzida)
    traducao = traducao_comando.translate(texto)
    texto_get.set(traducao)
#FUNÇÃO PARA INVERTER OS IDIOMAS TRADUZIR-TRADUZIDO
def inverter_lingua_traducao():
    lingua_um = lingua_traduzir.get()
    lingua_dois = lingua_traduzida.get()
    lingua_traduzida.set(lingua_um)
    lingua_traduzir.set(lingua_dois)
    
    traduzir = caixa_traduzir.get()
    traduzido = texto_get.get()
    caixa_traduzir.delete(0,END)
    caixa_traduzir.insert(0, traduzido)
    texto_get.set(traduzir)

#FUNÇÃO PARA SALVAR O AUDIO DO TEXTO TRADUZIDO
'''PS: ESSE BOTÃO APENAS SALVA O AUDIO EM MP3, ELE NÃO REPRODUZ O MESMO NA INTERFACE'''
def ler_traducao():
    texto_para_ler = texto_get.get()
    lingua_da_leitura = lingua_traduzida.get()

    leitura = gtts.gTTS(text=texto_para_ler, lang=lingua_da_leitura, slow=False)
    leitura.save('leitura.mp3')
    

#IDIOMAS PARA TRADUZIR
ln = ['pt','fr','en','jp','ko','ru','de','ar']

#CUSTOMIZAÇÃO DA INTERFACE 
win = Tk()
win.title('Meu tradutor')
texto_get = StringVar()
win.geometry('600x500')
win.maxsize(600,500)
win.minsize(600,500)

texto_traduzir = Label(text='Texto para traduzir: ', font=('Aryal 10 bold'))
texto_traduzir.place(x=10,y=10)

lingua_traduzir = ttk.Combobox(values=ln)
lingua_traduzir.place(x=150, y=10)

caixa_traduzir = Entry(win, width=65,  font=('Aryal 10 bold'), relief='raised')
caixa_traduzir.pack(pady=50, ipady=70)

button_traduzir = Button(text='Traduzir', command=texto_translate,width=10, relief=RAISED, overrelief=RIDGE, font=('Aryal 8 bold'))
button_traduzir.place(x=200, y=230)

inverter_lingua = Button(text='Inverter', command= inverter_lingua_traducao, width=10, relief=RAISED, overrelief=RIDGE, font=('Aryal 8 bold'))
inverter_lingua.place(x=290, y=230)

ler = Button(text='Salvar Audio', command= ler_traducao, width=10, relief=RAISED, overrelief=RIDGE, font=('Aryal 8 bold'))
ler.place(x=380, y=230)




texto_traduzido = Label(text='Texto da Tradução: ', font=('Aryal 10 bold'))
texto_traduzido.place(x=10,y=270)

lingua_traduzida = ttk.Combobox(values=ln)
lingua_traduzida.place(x=150, y=270)

caixa_traduzida = Label(win, width=57, textvariable= texto_get ,font=('Aryal 10 bold'), height=11, bg='#FFF', relief='raised', anchor='nw')
caixa_traduzida.pack(pady=50, ipady=70)

win.mainloop()
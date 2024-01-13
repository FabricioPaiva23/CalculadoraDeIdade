from tkinter import *
from tkcalendar import Calendar, DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date


janela = Tk()
janela.title("Calculadora de idade")
janela.geometry('310x430')

#--------Cores------------

cor1 = "#3b3b3b"
cor2 = "#333333"
cor3 = "#ffffff"
cor4 = "#ffa500"

#--------Frames------------

frame_cima = Frame(janela, width=310, height=140, pady=0, padx=0, relief=FLAT, bg=cor2)
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=290, pady=0, padx=0, relief=FLAT, bg=cor1)
frame_baixo.grid(row=1, column=0)

#-------Labels-------------

l_calculadora = Label(frame_cima, text="CALCULADORA", width=25, height=1, padx=3, relief=FLAT, anchor=NW, font=("Ivi 25 bold"), bg=cor2, fg=cor3)
l_calculadora.place(x=25, y=30)

l_idade = Label(frame_cima, text="DE IDADE", width=11, height=1, padx=0, relief=FLAT, anchor=NW, font=("Arial 35 bold"), bg=cor2, fg=cor4)
l_idade.place(x=40, y=70)


#-----Função calcular idade------

def calcular():
    inicial = cal_1.get()
    final = cal_2.get()
    
    dia_inicial, mes_inicial, ano_inicial = [int(f) for f in inicial.split('/')]
    dia_final, mes_final, ano_final = [int(g) for g in final.split('/')]
    
    data_inicial = date(ano_inicial, mes_inicial, dia_inicial)
    data_final = date(ano_final, mes_final, dia_final)
    
    anos = relativedelta(data_inicial, data_final).years
    meses = relativedelta(data_inicial, data_final).months
    dias = relativedelta(data_inicial, data_final).days
    
    l_ano['text'] = anos
    l_mes['text'] = meses
    l_dia['text'] = dias
    

#-------Labels-------------


l_data_inicial = Label(frame_baixo, text="Data inicial", height=1, padx=0, pady=0, relief=FLAT, anchor=NW, font=("Ivi 11"), bg=cor1, fg=cor3)
l_data_inicial.place(x=35, y=30)

cal_1 = DateEntry(frame_baixo, width=13, bg='darkblue', fg=cor3, borderwidth=2, date_patter='dd/mm/y', Y=2024 )
cal_1.place(x=170, y=30)

l_data_nascimento = Label(frame_baixo, text="Data nascimento", height=1, padx=0, pady=0, relief=FLAT, anchor=NW, font=("Ivi 11"), bg=cor1, fg=cor3)
l_data_nascimento.place(x=35, y=70)

cal_2 = DateEntry(frame_baixo, width=13, bg='darkblue', fg=cor3, borderwidth=2, date_patter='dd/mm/y', Y=2024 )
cal_2.place(x=170, y=70)



#----- Labels resultado ------

l_ano = Label(frame_baixo, text="--", height=1, padx=0, pady=0, relief=FLAT, anchor=CENTER, font=("Ivi 20 bold"), bg=cor1, fg=cor3)
l_ano.place(x=50, y=115)

l_mes = Label(frame_baixo, text="--", height=1, padx=0, pady=0, relief=FLAT, anchor=CENTER, font=("Ivi 20 bold"), bg=cor1, fg=cor3)
l_mes.place(x=130, y=115)

l_dia = Label(frame_baixo, text="--", height=1, padx=0, pady=0, relief=FLAT, anchor=CENTER, font=("Ivi 20 bold"), bg=cor1, fg=cor3)
l_dia.place(x=210, y=115)

l_ano_text = Label(frame_baixo, text="ANOS", height=1, padx=0, pady=0, relief=FLAT, anchor=CENTER, font=("Ivi 13"), bg=cor1, fg=cor3)
l_ano_text.place(x=40, y=160)

l_meses_text = Label(frame_baixo, text="MESES", height=1, padx=0, pady=0, relief=FLAT, anchor=CENTER, font=("Ivi 13"), bg=cor1, fg=cor3)
l_meses_text.place(x=118, y=160)

l_dias_text = Label(frame_baixo, text="DIAS", height=1, padx=0, pady=0, relief=FLAT, anchor=CENTER, font=("Ivi 13"), bg=cor1, fg=cor3)
l_dias_text.place(x=205, y=160)



#------botao----------

botao_calcular = Button(frame_baixo, text="Calcular", height=1, width=20, relief='raised', overrelief='ridge',font=("Ivi 10 bold"), bg=cor1, fg=cor3, command=calcular)
botao_calcular.place(x=50, y=200)


#------rodapé---------

l_rodape = Label(frame_baixo, text="Desenvolvido por Fabricio Paiva", height=1, padx=0, pady=0, relief=FLAT, anchor=CENTER, font=("Ivi 10"), bg=cor1, fg=cor4)
l_rodape.place(x=43, y=260)


janela.mainloop()


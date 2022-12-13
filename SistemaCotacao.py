import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter.filedialog import askopenfilename
import pandas as pd
import requests
from datetime import datetime
import numpy as np


requisicao = requests.get('https://economia.awesomeapi.com.br/json/all')
dicionario_moedas = requisicao.json()

lista_moedas = list(dicionario_moedas.keys())


def pegar_cotacao():
    moeda = combobox_selecioneamoeda.get()
    data_cotacao = calendario_moeda.get()
    ano = data_cotacao[-4:]
    mes = data_cotacao[3:5]
    dia = data_cotacao[:2]
    link = f'https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL?' \
           f'start_date={ano}{mes}{dia}&end_date={ano}{mes}{dia}'
    requisicao_moeda = requests.get(link)
    cotacao = requisicao_moeda.json()
    valor_moeda = cotacao[0]['bid']
    label_textocotacao['text'] = f'A cotação da {moeda} no dia {data_cotacao} foi de: R${valor_moeda}'


def selecionar_arquivo():
    caminho_arquivo = askopenfilename(title='Selecione o Arquivo de Moeda')
    var_caminhoarquivo.set(caminho_arquivo)
    if caminho_arquivo:
        label_arquivoselecionado['text'] = f'Arquivo Selecionado: {caminho_arquivo}'


def atualizar_cotacoes():
    try:
        df = pd.read_excel(var_caminhoarquivo.get())
        moedas = df.iloc[:, 0]
        data_inicial = calendario_datainicial.get()
        data_final = calendario_datafinal.get()

        ano_inicial = data_inicial[-4:]
        mes_inicial = data_inicial[3:5]
        dia_inicial = data_inicial[:2]

        ano_final = data_final[-4:]
        mes_final = data_final[3:5]
        dia_final = data_final[:2]

        for moeda in moedas:
            link = f'https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL?' \
                   f'start_date={ano_inicial}{mes_inicial}{dia_inicial}&' \
                   f'end_date={ano_final}{mes_final}{dia_final}'

            requisicao_moeda = requests.get(link)
            cotacoes = requisicao_moeda.json()
            for cotacao in cotacoes:
                timestamp = int(cotacao['timestamp'])
                bid = float(cotacao['bid'])
                data = datetime.fromtimestamp(timestamp)
                data = data.strftime('%d/%m/%Y')
                if data not in df:
                    df[data] = np.nan

                df.loc[df.iloc[:, 0] == moeda, data] = bid

        df.to_excel('Teste.xlsx')
        label_atualizarcotacaoes['text'] = 'Arquivo atualizado com sucesso'
    except:
        label_atualizarcotacaoes['text'] = 'Selecione um arquivo Excel no formato correto'


janela = tk.Tk()

janela.title('Ferramenta de Cotação de Moeadas')

label_cotacaomoeda = tk.Label(text='Cotação de 1 moeda específica', borderwidth=2, relief='solid')
label_cotacaomoeda.grid(row=0, column=0, padx=10, pady=10, sticky='NSEW', columnspan=3)

label_selecionarmoeda = tk.Label(text='Selecionar moeda', anchor='e')
label_selecionarmoeda.grid(row=1, column=0, padx=10, pady=10, sticky='NSEW', columnspan=2)

combobox_selecioneamoeda = ttk.Combobox(values=lista_moedas)
combobox_selecioneamoeda.grid(row=1, column=2, padx=10, pady=10, sticky='NSEW')

label_selecionardia = tk.Label(text='Selecione o dia que deseja pegar a moeda', anchor='e')
label_selecionardia.grid(row=2, column=0, padx=10, pady=10, sticky='NSEW', columnspan=2)

calendario_moeda = DateEntry(year=2022, locale='pt_br')
calendario_moeda.grid(row=2, column=2, padx=10, pady=10, sticky='NSEW')

label_textocotacao = tk.Label(text='')
label_textocotacao.grid(row=3, column=0, padx=10, pady=10, sticky='NSEW', columnspan=2)

botao_pegarcotacao = tk.Button(text='Pegar Cotação', command=pegar_cotacao)
botao_pegarcotacao.grid(row=3, column=2, padx=10, pady=10, sticky='NSEW')

#Cotação de várias moedas
label_cotacaovariasmoedas = tk.Label(text='Cotação de múltiplas moedas', borderwidth=2, relief='solid')
label_cotacaovariasmoedas.grid(row=4, column=0, padx=10, pady=10, sticky='NSEW', columnspan=3)

label_selecionararquivo = tk.Label(text='Selecione um arquivo Excel com as moedas da coluna A')
label_selecionararquivo.grid(row=5, column=0, padx=10, pady=10, sticky='NSEW', columnspan=2)

var_caminhoarquivo = tk.StringVar()

botao_selecionararquivo = tk.Button(text='Clique para Selecionar', command=selecionar_arquivo)
botao_selecionararquivo.grid(row=5, column=2, padx=10, pady=10, sticky='NSEW')

label_arquivoselecionado = tk.Label(text='Nenhum Arquivo Selecionado', anchor='e')
label_arquivoselecionado.grid(row=6, column=0, padx=10, pady=10, sticky='NSEW', columnspan=3)

label_datainicial = tk.Label(text='Data Inicial', anchor='e')
label_datafinal = tk.Label(text='Data Final', anchor='e')
label_datainicial.grid(row=7, column=0, padx=10, pady=10, sticky='NSEW')
label_datafinal.grid(row=8, column=0, padx=10, pady=10, sticky='NSEW')

calendario_datainicial = DateEntry(year=2022, locale='pt_br')
calendario_datafinal = DateEntry(year=2022, locale='pt_br')
calendario_datainicial.grid(row=7, column=1, padx=10, pady=10, sticky='NSEW')
calendario_datafinal.grid(row=8, column=1, padx=10, pady=10, sticky='NSEW')

label_atualizarcotacoes = tk.Button(text='Atualizar cotações', command=atualizar_cotacoes)
label_atualizarcotacoes.grid(row=9, column=0, padx=10, pady=10, sticky='NSEW')

label_atualizarcotacaoes = tk.Label(text='')
label_atualizarcotacaoes.grid(row=9, column=1, padx=10, pady=10, sticky='NSEW', columnspan=2)

botao_fechar = tk.Button(text='Fechar', command=janela.quit)
botao_fechar.grid(row=10, column=2, padx=10, pady=10, sticky='NSEW')


janela.mainloop()
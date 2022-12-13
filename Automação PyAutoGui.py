#Neste exemplo são comandos com automação com pyautogui onde fora extraído uma base de dados num link do google drive.

import pyautogui
import pyperclip
import time

# Entrar no link (sistema)
pyautogui.hotkey('ctrl', 't') #hotkey serve para combinar teclar
pyperclip.copy('https://drive.google.com/drive/folders...') #
pyautogui.hotkey('ctrl', 'v') #hotkey serve para combinar letras
pyautogui.press('enter') #press para pressionar/apertar algo

time.sleep(3) #tempo para aguardar a página carregar

# Navegar até o local do relatório (entrar na pasta exportar)
pyautogui.click(x=387, y=269, clicks=2) #posição retirada do pyautogui.position e colocado o clicks 2 para entrar na opção
time.sleep(2)

# Fazer o download do relatório
pyautogui.click(x=402, y=374, clicks=1)
time.sleep(2)
pyautogui.click(x=1155, y=164, clicks=1)
time.sleep(2)
pyautogui.click(x=962, y=574, clicks=1)
time.sleep(5)

# Calcular os indicadores importei o pandas para realizar os trâmites da base em excel
import pandas as pd

tabela = pd.read_excel(r'C:\\Users\###\Downloads\Vendas - Dez.xlsx')
display(tabela)
faturamento = tabela['Valor Final'].sum()
quantidade = tabela['Quantidade'].sum()

# Entrar no email
pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://mail.google.com/m....')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(3)

pyautogui.click(x=98, y=176)

# Enviar por email o resultado
time.sleep(1)
pyautogui.write('fileme71@gmail.com')
pyautogui.press('tab')
pyautogui.press('tab')
pyperclip.copy('Relatório Pyhton')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')

texto = f''' Prezados, bom dia!

O faturamento foi de: R$ {faturamento:,.2f}
E a quantidade foi de: {quantidade:,}

Tmj, Fileme! '''

pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# pegar a cotação do dolar
navegador = webdriver.Chrome('chromedriver.exe')
navegador.get('https://www.google.com/')

navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dólar')

navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_dolar = navegador.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

# pegar a cotação do euro
navegador.get('https://www.google.com/')

navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação euro')

navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_euro = navegador.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

# pegar a cotação do ouro
navegador.get('https://www.melhorcambio.com/ouro-hoje')

cotacao_ouro = navegador.find_element_by_xpath('//*[@id="comercial"]').get_attribute('value')

cotacao_ouro = cotacao_ouro.replace(',', '.')

import pandas as pd
tabela = pd.read_excel('Produtos.xlsx')
display(tabela)

# atualizar a cotação, o preço de compra e o preço de venda

# atualizar a cotação
tabela.loc[tabela['Moeda'] == 'Dólar', 'Cotação'] = float(cotacao_dolar)
tabela.loc[tabela['Moeda'] == 'Euro', 'Cotação'] = float(cotacao_euro)
tabela.loc[tabela['Moeda'] == 'Ouro', 'Cotação'] = float(cotacao_ouro)

# atualizar o preço de compra (preço original * cotação)
tabela['Preço de Compra'] = tabela['Preço Original'] * tabela['Cotação']

# atualizar o preço de venda ( preço de compra * margem)
tabela['Preço de Venda'] = tabela['Preço de Compra'] * tabela['Margem']

tabela['Preço de Venda'] = tabela['Preço de Venda'].map('R$ {:.2f}'.format)

display(tabela)

# Exportar para o relatório atualizado

tabela.to_excel('Produto Novo.xlsx', index=False)
navegador.quit()
# Extração / Obtenção de dados

import pandas as pd

tabela = pd.read_csv('advertising.csv')

display(tabela)

# Análise exploratória
# descobrir a correlação dentro da tabela
# por meio de gráficos

import seaborn as sns
import matplotlib.pyplot as plt

sns.pairplot(tabela) # criando o gráfico
plt.show() #mostrando o gráfico

sns.heatmap(tabela.corr(), cmap='Wistia', annot=True) #criando mapa de calor o cmap é opcional para as cores
# annot = true também é opcional, mas ele mostra os valores dentro do mapa
plt.show() #motrando o gráfico

# na inteligencia artificial o x é tudo que você quer, sem a previsão (y) calculo sem o y
# y é quem você quer prever ( quem eu quero calcular)
# neste exemplo o y é a venda ( o que queremos ) e o x são os produtos (radio, tv, jornal)

# Modelagem + algoritmo

from sklearn.model_selection import train_test_split

y = tabela['Vendas']
x = tabela[['TV', 'Radio', 'Jornal']]

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)

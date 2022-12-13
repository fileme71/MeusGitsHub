# Coletando várias tabelas e fazendo análises

import pandas as pd

vendas_df = pd.read_csv('Contoso - Vendas  - 2017.csv', sep=';')
produtos_df = pd.read_csv('Contoso - Cadastro Produtos.csv', sep=';')
lojas_df = pd.read_csv('Contoso - Lojas.csv', sep=';')
clientes_df = pd.read_csv('Contoso - Clientes.csv', sep=';')

display(vendas_df)
display(produtos_df)
display(lojas_df)
display(clientes_df)

# pegando somente as colunas que queremos

clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'Nome do Produto']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]
display(lojas_df)

# PARA JUNTARMOS TABELAS (DATAFRAMES) UTILIZAREMOS O COMANDO MERGE
vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente')
display(vendas_df)

# renomear alguma coluna para ficar mais intuitivo no dataframe

vendas_df = vendas_df.rename(columns={'E-mail': 'E-mail do Cliente'})
display(vendas_df)

# Contando quantas vezes cada email aparece

frequencia_clientes = vendas_df['E-mail do Cliente'].value_counts()
display(frequencia_clientes)
frequencia_clientes[:5].plot(figsize=(15, 5))

# qual loja que mais vendeu em quantidade
# o groupby transforma o nome da loja no indice e depois nao precisa mencionar ele pra reduzir a tabela
vendas_lojas = vendas_df.groupby('Nome da Loja').sum()
vendas_lojas = vendas_lojas[['Quantidade Vendida']]
display(vendas_lojas)

# ordenando o dataframe
vendas_lojas = vendas_lojas.sort_values('Quantidade Vendida', ascending=False)
display(vendas_lojas)
# podemos plotar um gráfico pegando apenas as cinco primeiras
vendas_lojas[:5].plot(figsize=(15, 5), kind='bar') #kind é pra colocar o gráfico de barras

#pegando o maior valor e o melhor índice

maior_valor = vendas_lojas['Quantidade Vendida'].max() #maior valor
melhor_loja = vendas_lojas['Quantidade Vendida'].idxmax()
print(melhor_loja, maior_valor)

#pegando o menor valor de outra forma
menor_valor = vendas_lojas[-1:]
display(menor_valor)

# Filtrando um DATAFRAME

# Qual a porcentagem das vendas devolvidas?

qtde_vendida = vendas_df['Quantidade Vendida'].sum()
qtde_devolvida = vendas_df['Quantidade Devolvida'].sum()

print('{:.2%}'.format(qtde_devolvida / qtde_vendida))

# ESSA CONTA FOI PARA TODAS AS LOJAS

# filtrando LOJAS ESPECÍFICAS

loja_contoso_online = vendas_df[vendas_df['ID Loja'] == 306]
display(loja_contoso_online)

lojas_contoso_online = vendas_df[vendas_df['ID Loja'] == 306]
qtde_vendida = lojas_contoso_online['Quantidade Vendida'].sum()
qtde_devolvida = lojas_contoso_online['Quantidade Devolvida'].sum()

print('{:.2%}'.format(qtde_devolvida / qtde_vendida))

# constatamos que essa loja está acima da média

# junto
df_loja306sem0 = vendas_df[(vendas_df['ID Loja'] == 306) & (vendas_df['Quantidade Devolvida'] == 0)]
display(df_loja306sem0)
# separado
loja306 = vendas_df['ID Loja'] == 306
quantidade0 = vendas_df['Quantidade Devolvida'] == 0
df_total = vendas_df[loja306 & quantidade0]
display(df_total)


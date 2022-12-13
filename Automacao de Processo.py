#!/usr/bin/env python
# coding: utf-8

# ### Passo 1 - Importar Arquivos e Bibliotecas

# In[27]:


# importar biblioteca
import pandas as pd # biblioteca usada para análise de dados e manipulação de arquivos
import win32com.client as win32 # integração com windons para envio de e-mails
import pathlib # integra arquivos do pc com os comandos 


# In[28]:


# importar base de dados
emails = pd.read_excel(r'Bases de Dados\Emails.xlsx')
lojas = pd.read_csv(r'Bases de Dados\Lojas.csv', encoding='latin1', sep=';')
vendas = pd.read_excel(r'Bases de Dados\Vendas.xlsx')
display(emails)
display(lojas)
display(vendas)


# ### Passo 2 - Definir Criar uma Tabela para cada Loja e Definir o dia do Indicador

# In[29]:


# incluir o nome da loja em vendas
vendas = vendas.merge(lojas, on='ID Loja')
display(vendas)


# In[30]:


dicionario_lojas = dict() #criando um dicionário para armazenar as lojas
for loja in lojas['Loja']: # percorrer todas as lojas da tabela de lojas
    dicionario_lojas[loja] = vendas.loc[vendas['Loja']==loja, :] # criando e localizando cada loja para seus respectivos valores
display(dicionario_lojas['Shopping Midway Mall'])
display(dicionario_lojas['Salvador Shopping'])


# In[31]:


dia_indicador = vendas['Data'].max() # pegando o último dia da tabela
print(dia_indicador)


# ### Passo 3 - Salvar a planilha na pasta de backup

# In[32]:


#identificar se a pasta já existe

caminho_backup = pathlib.Path(r'Backup Arquivos Lojas')

arquivos_pasta_backup = caminho_backup.iterdir() # iterdir pegar os arquivos que estão dentro de uma pasta

lista_nomes_backup = [arquivo.name for arquivo in arquivos_pasta_backup] #podemos fazer com list comprehension
#for arquivo in arquivos_pasta_backup:
#    lista_nomes_backup.append(arquivo.name)

for loja in dicionario_lojas: # percorrendo as lojas do dicionário
    if loja not in lista_nomes_backup: # se na pasta do backup NÃO tiver uma pasta com o mesmo nome, então ela será criada 
        nova_pasta = caminho_backup / loja #criando a loja dessa forma por causa do pathlib
        nova_pasta.mkdir() # comando que cria as pastas
  
    #salvar dentro da pasta
    nome_arquivo = '{}_{}_{}.xlsx'.format(dia_indicador.month, dia_indicador.day, loja)
    local_arquivo = caminho_backup / loja / nome_arquivo
    dicionario_lojas[loja].to_excel(local_arquivo) #este dataframe manda esse arquivo para este caminho


# ### Passo 4 - Calcular o indicador para 1 loja

# In[33]:


# definição das metas

meta_faturamento_dia = 1000
meta_faturamento_ano = 165000
meta_qtdeprodutos_dia = 4
meta_qtdeprodutos_ano = 120
meta_ticketmedio_dia = 500
meta_ticketmedio_ano = 500


# In[34]:


for loja in dicionario_lojas:

    vendas_loja = dicionario_lojas[loja]
    vendas_loja_dia = vendas_loja.loc[vendas_loja['Data']==dia_indicador, :] #onde as linhas das datas é igual ao indicador

    # faturamento
    faturamento_ano = vendas_loja['Valor Final'].sum() #faturamento anual
    #print(faturamento_ano)
    faturamento_dia = vendas_loja_dia['Valor Final'].sum() #faturamento do dia
    #print(faturamento_dia)

    # diversidade de produtos
    qtde_produtos_ano = len(vendas_loja['Produto'].unique()) #pegando valores únicos o len no final foi pra saber o tamanho dessa lista
    qtde_produtos_dia = len(vendas_loja_dia['Produto'].unique())

    # ticket médio
    valor_venda = vendas_loja.groupby('Código Venda').sum() # vai agrupar a coluna código da venda e somar
    #display(valor_venda) visualizando só pra saber o resultado
    ticket_medio_ano = valor_venda['Valor Final'].mean() #agora sim, depois de somado que a gente consegue pegar a média
    #print(ticket_medio_ano)
    valor_venda_dia = vendas_loja_dia.groupby('Código Venda').sum()
    ticket_medio_dia = valor_venda_dia['Valor Final'].mean()
    #print(ticket_medio_dia)
    
    #enviar o email
    outlook = win32.Dispatch('outlook.application')

    nome = emails.loc[emails['Loja'] == loja, 'Gerente'].values[0]
    mail = outlook.CreateItem(0)
    mail.To = emails.loc[emails['Loja'] == loja, 'E-mail'].values[0]
    mail.Subject = 'OnePage Dia {}/{} - loja {}'.format(dia_indicador.day, dia_indicador.month, loja)
    # mail.Body = 'Texto do E-mail' -- opção direta ou opção em HTML

    if faturamento_dia >= meta_faturamento_dia:
        cor_fat_dia = 'green'
    else:
        cor_fat_dia = 'red'
    if faturamento_ano >= meta_faturamento_ano:
        cor_fat_ano = 'green'
    else:
        cor_fat_ano = 'red'
    if qtde_produtos_dia >= meta_qtdeprodutos_dia:
        cor_qtde_dia = 'green'
    else:
        cor_qtde_dia = 'red'
    if qtde_produtos_ano >= meta_qtdeprodutos_ano:
        cor_qtde_ano = 'green'
    else:
        cor_qtde_ano = 'red'
    if ticket_medio_dia >= meta_ticketmedio_dia:
        cor_ticket_dia = 'green'
    else:
        cor_ticket_dia = 'red'
    if ticket_medio_ano >= meta_ticketmedio_ano:
        cor_ticket_ano = 'green'
    else:
        cor_ticket_ano = 'red'

    mail.HTMLBody = f'''
    <p> Bom dia, {nome} </p>

    <p> O resultado de ontem <strong>({dia_indicador.day}/{dia_indicador.month})</strong> da <strong>loja {loja}</strong> foi de: </p>

    <table>
      <tr>
        <th>Indicador</th>
        <th>Valor Dia</th>
        <th>Meta Dia</th>
        <th>Cenário Dia</th>
      </tr>
      <tr>
        <td>Faturamento</td>
        <td style="text-align: center">R${faturamento_dia:.2f}</td>
        <td style="text-align: center">R${meta_faturamento_dia:.2f}</td>
        <td style="text-align: center"><font color="{cor_fat_dia}">◙</font></td>
      </tr>
      <tr>
        <td>Diversidade de Produtos</td>
        <td style="text-align: center">{qtde_produtos_dia}</td>
        <td style="text-align: center">{meta_qtdeprodutos_dia}</td>
        <td style="text-align: center"><font color="{cor_qtde_dia}">◙</font></td>
      </tr>
      <tr>
        <td>Ticket Médio</td>
        <td style="text-align: center">R${ticket_medio_dia:.2f}</td>
        <td style="text-align: center">R${meta_ticketmedio_dia:.2f}</td>
        <td style="text-align: center"><font color="{cor_ticket_dia}">◙</font></td>
      </tr>
    </table>
    <br>
    <table>
      <tr>
        <th>Indicador</th>
        <th>Valor Ano</th>
        <th>Meta Ano</th>
        <th>Cenário Ano</th>
      </tr>
      <tr>
        <td>Faturamento</td>
        <td style="text-align: center">R${faturamento_ano:.2f}</td>
        <td style="text-align: center">R${meta_faturamento_ano:.2f}</td>
        <td style="text-align: center"><font color="{cor_fat_ano}">◙</font></td>
      </tr>
      <tr>
        <td>Diversidade de Produtos</td>
        <td style="text-align: center">{qtde_produtos_ano}</td>
        <td style="text-align: center">{meta_qtdeprodutos_ano}</td>
        <td style="text-align: center"><font color="{cor_qtde_ano}">◙</font></td>
      </tr>
      <tr>
        <td>Ticket Médio</td>
        <td style="text-align: center">R${ticket_medio_ano:.2f}</td>
        <td style="text-align: center">R${meta_ticketmedio_ano:.2f}</td>
        <td style="text-align: center"><font color="{cor_ticket_ano}">◙</font></td>
      </tr>
    </table>

    <p> Segue em anexo a planilha com todos os dados para mais detalhes: </p>

    <p> Qualquer dúvida estou à disposição. </p>

    <p> Att., Rodolpho Pimentel </p>
    '''

    # anexos (pode colocar quantos quiser)
    attachment = pathlib.Path.cwd() / caminho_backup / loja / f'{dia_indicador.month}_{dia_indicador.day}_{loja}.xlsx' # pathlib faz o caminho até o arquivo
    mail.Attachments.Add(str(attachment))

    mail.Send()
    print('E-mail da loja {} enviado'.format(loja))


# ### Passo 5 - Enviar por e-mail para o gerente

# ### Passo 6 - Automatizar todas as lojas

# ### Passo 7 - Criar ranking para diretoria

# In[43]:


# criando um ranking
# agrupango a tabela e somando (pegamos só as Lojas e o seu Faturamento)
faturamento_lojas = vendas.groupby('Loja')[['Loja', 'Valor Final']].sum()
faturamento_lojas_ano = faturamento_lojas.sort_values(by='Valor Final', ascending=False) #ordernar do maior para o menor
display(faturamento_lojas_ano)

#criando uma pasta excel para o ranking anual
nome_arquivo = '{}_{}_Ranking Anual.xlsx'.format(dia_indicador.month, dia_indicador.day, loja)
faturamento_lojas_ano.to_excel(r'Backup Arquivos Lojas\{}'.format(nome_arquivo))

vendas_dia = vendas.loc[vendas['Data']==dia_indicador, :]
faturamento_lojas_dia = vendas_dia.groupby('Loja')[['Loja', 'Valor Final']].sum()
faturamento_lojas_dia = faturamento_lojas_dia.sort_values(by='Valor Final', ascending=False)
display(faturamento_lojas_dia)

#criando uma pasta excel para o ranking diário
nome_arquivo = '{}_{}_Ranking Dia.xlsx'.format(dia_indicador.month, dia_indicador.day, loja)
faturamento_lojas_ano.to_excel(r'Backup Arquivos Lojas\{}'.format(nome_arquivo))


# ### Passo 8 - Enviar e-mail para diretoria

# In[46]:


# enviar e-mail para a diretoria
outlook = win32.Dispatch('outlook.application')

mail = outlook.CreateItem(0)
mail.To = emails.loc[emails['Loja'] == 'Diretoria', 'E-mail'].values[0]
mail.Subject = f'Ranking Dia {dia_indicador.day}/{dia_indicador.month}'
mail.Body = f'''
Prezados, bom dia!

Melhor dia Dia em faturamento: Loja {faturamento_lojas_dia.index[0]} com faturamento R${faturamento_lojas_dia.iloc[0, 0]:.2f}
Pior loja do Dia em faturamento: Loja {faturamento_lojas_dia.index[-1]} com faturamento R${faturamento_lojas_dia.iloc[-1, 0]:.2f}

Melhor loja do Ano em faturamento: Loja {faturamento_lojas_ano.index[0]} com faturamento R${faturamento_lojas_ano.iloc[0, 0]:.2f}
Pior loja do Ano em faturamento: Loja {faturamento_lojas_ano.index[-1]} com faturamento R${faturamento_lojas_ano.iloc[-1, 0]:.2f}

Seguem em anexo os rankings do ano e do dia de todas as lojas.

Qualquer dúvida estou à disposição.

Att.,
Rodolpho.    

'''

# anexos
attachment = pathlib.Path.cwd() / caminho_backup / f'{dia_indicador.month}_{dia_indicador.day}_Ranking Anual.xlsx'
mail.Attachments.Add(str(attachment))
attachment = pathlib.Path.cwd() / caminho_backup / f'{dia_indicador.month}_{dia_indicador.day}_Ranking Dia.xlsx'
mail.Attachments.Add(str(attachment))


mail.Send()
print('E-mail da Diretoria enviado')


# In[ ]:





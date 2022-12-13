# Práticando exercícios com Dicionários


mais_vendidos = {'tecnologia': 'iphone', 'refrigeracao': 'ar consul 12000 btu', 'livros': 'o alquimista', 'eletrodoméstico': 'geladeira', 'lazer': 'prancha surf'}

vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

# respondendo com a chave
print('O livro mais vendido foi {}'.format(mais_vendidos['livros']))
print(f'O celular mais vendido foi {mais_vendidos["tecnologia"]}')

# respondendo com o método get

print(vendas_tecnologia.get('tv samsung'))
print('As vendas do iphone foram de {}'.format(vendas_tecnologia.get('iphone')))

# Neste FOR vamos verificar todos os valores com suas respectivas chaves

for chave in vendas_tecnologia:
    print('{}: {} unidades'.format(chave, vendas_tecnologia[chave]))

# Exercício da média do aluno com dicionário

aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Qual foi a Média de {aluno["Nome"]}: '))

if aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado!'
elif 5 <= aluno['Media'] <= 7:
    aluno['Situação'] = 'Recuperação!'
else:
    aluno['Situação'] = 'Reprovado!'
print('-=' *30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')

# Calculando a aposentadoria

from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho: (0 não tem) '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano da contratação: '))
    dados['salário'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' *30)
for k, v in dados.items():
    print(f'{k} é {v}')


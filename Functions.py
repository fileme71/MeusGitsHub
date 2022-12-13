# Exercícios de funções

def aumentar(preco, taxa):
    res = preco + (preco * taxa / 100)
    return res


def diminuir(preco, taxa):
    res = preco - (preco * taxa / 100)
    return res


def dobro(preco):
    res = preco * 2
    return res


def metade(preco):
    res = preco / 2
    return res

# Verificando se já pode votar nas eleições

# Exercício 101

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return (f'Com {idade} anos, voto não é obrigatório!')
    elif 16 <= idade < 18 or idade > 65:
        return (f'Com {idade} anos, o voto é opcional!')
    else:
        return (f'Com {idade} anos, o voto é obrigatório!')


nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))

# Clientes devedores

lista_devedores = [('123.123.123-12', 1300, 24), ('321.312.312-21', 1400, 19), ('156.987.123-56', 2300, 24)]

def clientes_inadimplentes(clientes_devedores):
    lista_clientes = []
    for cliente in clientes_devedores:
        cpf, valor, dias = cliente
        if valor > 1000 and dias > 20:
            lista_clientes.append(cpf)
    return lista_clientes

print(clientes_inadimplentes(lista_devedores))

# Padronização de produtos

# Exercício para padronizar se escolhe em minúsculo ou maiúsculo

def padronizar_codigos(lista_codigos, padrao='m'):
    for i, item in enumerate(lista_codigos):
        item = item.replace('  ', ' ')
        item = item.strip()
        if padrao == 'm':
            item = item.casefold()
        elif padrao == 'M':
            item = item.upper()
        lista_codigos[i] = item
    return lista_codigos


codigos = ['Abc123', 'BEF321', 'fff432']
print(padronizar_codigos(codigos, 'M'))


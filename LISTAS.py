# Neste exercício foi realizado uma separação de valores pares e ímpares. Posteriormente, printei os resultados e os coloquei em ordem crescente

lista = [[], []]
valor = 0
cont = 0
for c in range(1, 8):
    valor = int(input('Digite os valores: '))
    if valor % 2 == 0:
        lista[0].append(valor)
        cont += 1
    else:
        lista[1].append(valor)
        cont += 1
print(f'Todos os valores da lista são {lista}')
lista[0].sort()
print(lista[0])
lista[1].sort()
print(lista[1])

# Esquema real de ferramenta de trabalho

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

vendas_1sem.extend(vendas_2sem)
maior_valor = max(vendas_1sem)
menor_valor = min(vendas_1sem)

i1 = vendas_1sem.index(maior_valor)
i2 = vendas_1sem.index(menor_valor)
fat_total = sum(vendas_1sem)
print('O melhor mes foi {} e o valor foi {} ' .format(meses[i1], maior_valor))
print('O pior mes foi {} e o valor foi {} ' .format(meses[i2], menor_valor))
print('O faturamento total foi de R${:,} '.format(fat_total))

percentual = maior_valor / fat_total
print('O percentual foi de {:.1%} ' .format(percentual))
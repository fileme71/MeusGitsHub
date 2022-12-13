# Simulação de pagamento em mercado

forma = input('Qual será a forma de pagamento?\n'
               '<D> para dinheiro e cheque\n'
               '<C> para cartão a vista\n'
               '<P> para parcelado\n'
               '<J> parcelado com juros ').upper()
preco = float(input('Qual é o preco do produto? '))

if forma == 'D':
    total = preco - (preco * 10 / 100)
elif forma == 'C':
    total = preco - (preco * 5 / 100)
elif forma == 'P':
    total = preco
    parcela = total / 2
    print('Sua parcela será em 2x de {}'.format(parcela))
elif forma == 'J':
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('O total de parcela foi {} e o valor ficou em R${} com juros'.format(totalparc, parcela))
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))

# Jogo de Pedra, Papel e Tesoura

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,3)
print(''' FAÇA A SUA JOGADA!
[1] PEDRA
[2] PAPEL
[3] TESOURA
      ''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('Poo!!!')
sleep(1)
print('-=' *11)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-=' *11)
if computador == 0:
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Jogador, vence!')
    elif jogador == 2:
        print('Computador, vence!')
    else:
        print('Jogada inválida')
if computador == 1:
    if jogador == 0:
        print('Computador, vence!')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador, vence!')
    else:
        print('Jogada inválida')
if computador == 2:
    if jogador == 0:
        print('Jogador, vence!')
    elif jogador == 1:
        print('Computador, vence!')
    elif jogador == 2:
        print('Empate!')
    else:
        print('Jogada inválida')

# Verificando se um número é primo

num = int(input('Digite o numero: '))
total = 0

for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end = '')
    print('{}'.format(c), end= '')
print('\n\033[mO numero foi {} é divisível {} de vezes'.format(num, total))
if total == 2:
    print('Logo, este número é primo!')
else:
    print('Então, este número não é primo!')


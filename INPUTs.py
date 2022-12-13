#Nesta atividade eu fiz um simples input e uma série de prints para trazer resultados dos seus variados tipos

a = str(input('Qual é a sua profissão: '))
#type(profissao)
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É um alfabeto? ', a.isalpha())
print('É um alfanumérico? ', a.isalnum())
print('Está em maiúsculo? ', a.isupper())
print('Está em minúsculo? ', a.islower())
print('Está capitalizada? ', a.istitle())

#Exercício de ótima importância para a prática do uso de resultados em conjunto

nota1 = float(input('Digite a nota1: '))
nota2 = float(input('Digite a nota2 '))
media = float((nota1+nota2)/2)

if media >= 7:
    print('O aluno ficou com a média de {} e passou de ano! ' .format(media))
elif media >= 6:
    print('O aluno está de recuperação, pois está com uma média de {}. ' .format(media))
else:
    print('O aluno repetiu de ano, pois sua média foi abaixo de 6. ')


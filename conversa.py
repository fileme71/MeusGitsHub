import speech_recognition as sr

rec = sr.Recognizer()

nome = ''
with sr.Microphone() as microfone:
    nome = str(input(f'Qual é o seu {nome}? '))
    rec.adjust_for_ambient_noise(microfone)
    rec.pause_threshold = 1
    rec.dynamic_energy_adjustment_ratio = 3
    print(f'Oi, {nome}, tudo bem? ')

    audio = rec.listen(microfone)

    texto = rec.recognize_google(audio, language='pt-BR')
    print(texto)

    if texto == "tudo bem":
        print('Boa! Então, você gosta de qual esporte? ')
    elif texto == 'não estou bem':
        print('Força aí, cara...')
    else:
        print('Qual é a sua comida preferida? ')

    audio = rec.listen(microfone)
    texto = rec.recognize_google(audio, language='pt-BR')
    print(texto)

    if texto == 'futebol':
        print('Ih... para! Sabe que o papai aqui é o CR7, né? Hahaha. Mas e aí, trabalha com algo?')
    elif texto == 'pizza':
        print('Caramba, a minha também! Mas e aí, trabalhando com algo? ')
    elif texto == 'mas estou melhorando':
        print('É isso aí, levanta a cabeça!, Tá trabalhando, pai?')
    else:
        print('Hmm... E os trabalhos, man?')

    audio = rec.listen(microfone)
    texto = rec.recognize_google(audio, language='pt-BR')
    print(texto)

    if texto == 'sou engenheiro de dados':
        print('Deu aula, irmão!')
    elif texto == 'quero ser engenheiro de dados':
        print('Vou te indicar para uma vaga aqui da empresa')
    else:
        print('Com essa cara aí? kkkk')

print('Fim da conversa!')
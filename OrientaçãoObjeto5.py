# Criando um sistema de banco

class ContaCorrente():

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0

    def consultar_saldo(self):
        print('Seu saldo é de R${:,.2f}'.format(self.saldo))

    def depositar_dinheiro(self, valor):
        self.saldo += valor
        print('Você depositou R${:,.2f}'.format(valor))
        self.consultar_saldo()

    def sacar_dinheiro(self, valor):
        if self.saldo - valor < 0:
            print('Você não tem dinheiro suficiente!')
            self.consultar_saldo()
        else:
            self.saldo -= valor
            print('Você sacou R${:,.2f}'.format(valor))


#programa
conta_rod = ContaCorrente("Rodolpho" , "123.123.123-12")
conta_rod.consultar_saldo()

#depositando dinheiro na conta
conta_rod.depositar_dinheiro(1500)

#sacando dinheiro da conta
conta_rod.sacar_dinheiro(800)

print('Saldo final: ', end='')
conta_rod.consultar_saldo()

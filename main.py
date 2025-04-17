# 1. Sistema Bancário Simples
# Crie uma classe ContaBancaria com atributos como número da conta, titular e saldo.
# Implemente métodos para depositar, sacar e exibir saldo.
# Crie uma subclasse ContaPoupanca com um método para aplicar juros ao saldo.


class ContaBancaria:
    def __init__(self, numconta: int, titular: str, saldo: float):
        self.numconta = numconta
        self.titular = titular
        self.saldo = saldo


    def depositar(self, valordeposito: float):
        if valordeposito > 0:
            self.saldo += valordeposito
            return self.saldo

    def sacar(self, valorsaque: float):
        if valorsaque > 0:
            self.saldo -= valorsaque
            return self.saldo

    def exibir_saldo(self):
        print(self.saldo)


class ContaPoupanca(ContaBancaria):
    def aplica_juros(self, taxa_juros: float):
        if taxa_juros > 0:
            self.saldo += self.saldo * taxa_juros
            return self.saldo

conta = 3255
titular = "Keity Ranna"
saldo = 3582.55 
deposito = 300
saque = 50

caixa = ContaBancaria(conta,titular,saldo)
caixa.depositar(deposito)
caixa.sacar(saque)
caixa.exibir_saldo()

poup = ContaPoupanca(3255, "Keity Ranna", 5000.0)
poup.aplica_juros(0.05)  # Aplicando 5% de juros
poup.exibir_saldo()
        

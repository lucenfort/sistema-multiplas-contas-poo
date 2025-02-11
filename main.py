class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return f"{self.titular}: R$ {self.saldo}"

class SistemaBancario:
    def __init__(self):
        # Inicialize a lista de contas
        self.contas = []

    def criar_conta(self, titular, saldo):
        # Crie uma nova conta e adicione à lista de contas
        nova_conta = ContaBancaria(titular, saldo)
        self.contas.append(nova_conta)

    def listar_contas(self):
        # Liste todas as contas no formato "Titular: R$ Saldo", separadas por vírgula
        print(", ".join(str(conta) for conta in self.contas))

# Crie uma instância de SistemaBancario
sistema = SistemaBancario()

while True:
    entrada = input().strip()
    if entrada.upper() == "FIM":
        break
    titular, saldo = entrada.split(", ")
    sistema.criar_conta(titular, int(saldo))

sistema.listar_contas()

from model.ContaCorrente import ContaCorrente
from model.Banco import Banco

def main():
    conta = ContaCorrente(cpf_titular='119.143.139-84')
    print(conta.saldo)
    print(conta.numero_conta)
    print(conta.cpf_titular)

if __name__ == "__main__":
    main()

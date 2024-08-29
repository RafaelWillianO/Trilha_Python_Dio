menu = """

[d] depositar
[s] sacar
[e] extrato
[q] sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 1

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Qual o valor do depósito:  "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação Falhou! O valor informado é inválido")

    elif opcao == "s":
        valor = float(input("Informe o valo do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques > LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")

        elif excedeu_limite:
            print("Operação falhou! Limite insuficiente.")

        elif excedeu_saques:
            print("Operação falhou! Saques insuficiente.")

        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! Valor inválido.")

    elif opcao == "e":
        print("\n ==================== EXTRATO =====================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("=======================================================")
    elif opcao == "q":

        break

    else:
        print("Operação inválida, selecione nnovamente a operação desejada.")

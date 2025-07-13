menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor

            extrato += f"Depósito: R$ {valor:.2f}\n"

            print(f"Saldo atual: {saldo:.2f}")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":

        if numero_saques < LIMITE_SAQUES:

            valor = float(input("Informe o valor do saque: "))

            if valor > 0 and valor <= saldo and valor <= limite:

                numero_saques += 1

                saldo -= valor

                print(f"Você sacou R$ {valor:.2f}")

                extrato += f"Saque: R$ {valor:.2f}\n"

            else:
                print("Operação falhou! O valor informado é inválido.")
        
        else:
            print("Operação falhou! Limite de saques diários excedido.")

    elif opcao == "e":
        print(f"{extrato}\n")
        print(f"Saldo: R$ {saldo}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
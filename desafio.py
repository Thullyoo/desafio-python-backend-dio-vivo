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

    if  opcao == "d":
        valor_deposito = float(input("Quanto deseja depositar?\n"))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito de R${valor_deposito:.2f} concluído\n"
        else:
            print("Valor inválido para depósito")

    elif opcao == "s":
        if LIMITE_SAQUES  > 0:
            if saldo > 0:
                valor_saque = float(input("Quanto deseja sacar?\n"))
                if valor_saque > 0 and valor_saque <= limite:
                    saldo -= valor_saque
                    extrato += f"Sacou no valor de R${valor_saque:.2f}\n"
                    LIMITE_SAQUES -= 1
                else:
                    print("Valor inválido para saque")
            else:
                print("Saldo insuficiente para saque")
        else:
            print("Limite de saques diários excedido, não é póssivel sacar mais por hoje \n")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print(f"{extrato}\n" if extrato else "Não houve movimentações na conta")
        print(f"R${saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
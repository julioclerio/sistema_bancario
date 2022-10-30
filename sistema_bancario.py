
menu= """"
[d] Depositar
[s] Sacar 
[e] Extrato 
[q] Sair 

=>"""

saldo=0
limite=500
extrato= ""
numero_saques=0
limite_saques=3

while True:
    opcao = input(menu)
    
    
    if opcao == "d":
        deposito=float(input("Informe o valor do deposito: "))

        if deposito >0:
            saldo += deposito
            extrato += f"Deposito de R$ {deposito:.2f}\n"
            print("Deposito de R$ ",deposito," realizado com sucesso")

        else:
            print("Valor Inválido")



    elif opcao == "s":
        saque=float(input("Digite o valor do saque: "))

        if saque>limite:
            print("Valor excedito de R$500,00")
        elif numero_saques > limite_saques:
            print("número excedido de saques diários")
        elif saldo < saque:
            print("Saldo insuficiente")
        elif saque < 0:
            print("Valor inválido")
        else:
            saldo -= saque
            extrato += f"Saque de R$ {saque:.2f}\n"
            numero_saques += 1
            print("saque de R$", saque, "realizado com sucesso!")
    
    elif opcao == "e":
        print("==================Extrato Bancário==================")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print (f"\nSaldo: R$ {saldo: .2f} ")
        print("=====================================================")

    elif opcao == "q":
        break
    else:
        print("Opção inválida")





import os
def limpar():
    os.system("cls")
menu = f"""
===================OPÇÕES===================
Por favor selecione uma opção:
============================================
1-Sacar
2-Depositar
3-Extrato(Mostra o extrato bancário)
4-SAIR
============================================
:"""
saldo = 0
limite = 500
saques = 0
extrato = ""
LIMITE_SAQUE = 3

while True :

    opcao = input(menu)

    if opcao == "1" :

        limpar()
        print(f"""

=========SAQUE=========
Saldo disponivél R${saldo:.2f}
=======================              
Limite de saques:{LIMITE_SAQUE}
=======================
Saques feitos:{saques}
=======================
Limite para saque é de R${limite}""")
        valor = float(input("Insira o valor para saque: "))
        if valor <= 0:
            print("""
==========ERROR==========
Por favor insira um valor valido""")
        elif saques == LIMITE_SAQUE :
            print("Infelismente sua conta chegou ao limite de saques. Tente novamente amanhã quando o limite reiniciar ")
        elif valor > saldo : 
            print("""
==========ERROR==========
O valor do saque excedeu o seu saldo""")
        elif valor > limite:
            print("""
==========ERROR==========
O valor do saque excedeu o seu limite""")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f} \n"
            saques += 1
        elif valor != float():print("""
==========ERROR==========
Por favor insira um valor valido""")

    elif opcao == "2":

        limpar()
        print("""
=========DEPOSITAR=========
Defina o valor que deseja depositar R$""")
        valor = float(input())
        if valor > 0 :
            saldo += valor 
            extrato += f"Deposito: R${valor:.2f}\n"
        else:
            print("""
==========ERROR==========
Por favor insira um valor valido""")
    elif opcao == "3":
        limpar()
        print("=====================EXTRATO=====================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo atual R${saldo:.2f}")
        print("=================================================")
    elif opcao == "4" :
        limpar()
        print("""
===============================================OBRIGADO POR SER NOSSO CLIENTE===============================================

===============================================SAINDO...===============================================
""")
        break
    else:print("=================OPÇÃO INVÁLIDA=================")
num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro numero: "))
opcao = int(input("Informe a opção desejada, 1-somar, 2-subtrair, 3-multiplicar ou 4-dividir: "))

match opcao:
    case 1:
        total = num1 + num2
        print("A soma dos valores é : ", total)
    case 2:
        total = num1-num2
        print("A subtração dos valores é : ",total)
    case 3:
        total = num1*num2
        print("A multiplicação dos valores é : ",total)
    case 4:
        total = num1/num2
        print("A divisão dos valores é : ", total)
    case _:
        print("Opção invalida")
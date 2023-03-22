numero = float(input("Digite um numero: "))
opcao = int(input("Digite uma operação entre 1 a 3:  "))

match opcao:
    case 1:
        numero += 5
        print("O valor do numero + 5 ficou :",numero)
    case 2:
        numero -= 4
        print("O valor do numero -4 ficou: ", numero)
    case 3:
        numero *= 2
        print("O valor dobrado ficou: ", numero)
    case _:
        print("Opção invalida")

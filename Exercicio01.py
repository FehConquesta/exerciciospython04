codigo = int(input("Informe o codigo do produto desejado:"))

match codigo:
    case 1:
        print("O produto é a Caneta e o valor é R$1.20 ")
    case 2:
        print("O produto é o Lapis e o valor é R$0.80")
    case 3:
        print("O produto é o caderno e o valor é R$4.50")
    case 4:
        print("O produto é a borracha e o valor é R$1.00")
    case 5:
        print("O produto é a regua e o valor é R$1.50")
    case _:
        print("Numero invalido")

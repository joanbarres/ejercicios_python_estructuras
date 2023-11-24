print("Escriu 5 numeros i el mostrare el mes gran: ")
majorNumero = 0
numero = 0
valor = ""
while(True):
    valor = input()
    if(valor == "fi"):
        break
    else:
        numero = int(valor)
        if(numero > majorNumero):
            majorNumero = numero


print(majorNumero)
